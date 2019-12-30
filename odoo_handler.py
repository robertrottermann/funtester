#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import getpass
import psycopg2
import psycopg2.extras
from tools import BASE_PATH, MyNamespace, get_config_from_yaml
import urllib.request, urllib.error, urllib.parse
from bcolors import bcolors

def _construct_filter(filt):
    """construct a odoo search domain

    Arguments:
        filt {list of tuples} -- [(field_name, {comperator, '='}, value)]

    Returns:
        list of tuples -- serch domain
    """
    new_filt = []
    for elems in filt:
        if len(elems) == 2:
            new_filt.append((elems[0], '=', elems[1]))
        else:
            new_filt.append((elems[0], elems[1], elems[2]))

    return new_filt


def get_objects(module, what=["id"], filt=[], login=[], verbose=False):
    """get list of objects of a given type

    Arguments:
        module {string} -- what module to get objects from

    Keyword Arguments:
        what {list} -- which fields to return (default: {['id']})
        filter {list} -- filter to apply to find objects (default: {[]})
        verbose {bool} -- ..
    """
    result = []
    # get_objects migth be called in an eval(xxx) situation
    # where we want to use the actual environment with an odoo set
    handler = OdooHandler()
    odoo = handler.get_odoo(login=login)
    if not odoo:
        return
    env = odoo.env
    m = env[module]
    if filt:
        filt = _construct_filter(filt)
    objs = m.search(filt)
    for obj in m.browse(objs):
        res = ()
        if len(what) > 1:
            for e in what:
                res += obj.get(e)
            result.append(res)
        else:
            result.append(getattr(obj, what[0]))
    if verbose:
        print(module, result)
    return result


class OdooHandler(object):
    BASE_DEFAULTS = {}  # will be set when yaml was loaded

    _odoo = None
    opts = MyNamespace()
    # ---------------------------
    # access to odoo and postgres
    # ---------------------------
    @property
    def db_name(self):
        return self.BASE_DEFAULTS.get("db_name", "fernuni13")

    # rpc_host: on what host is odoo running
    @property
    def rpc_host(self):
        return self.BASE_DEFAULTS.get("rpc_host", "")

    # rpc_port what port is odoo using
    @property
    def rpc_port(self):
        return self.BASE_DEFAULTS.get("rpc_port", 8089)

    # rpc_user: as what user do we access odoo
    @property
    def rpc_user(self):
        return self.BASE_DEFAULTS.get("rpc_user", getpass.getuser())

    # rpc_user_pw: what is the odoo uses pw
    @property
    def rpc_user_pw(self):
        return self.BASE_DEFAULTS.get("rpc_user_pw", "admin")

    # db_user: as what user are we accessing postgres
    @property
    def db_user(self):
        return self.BASE_DEFAULTS.get("db_user", getpass.getuser())

    # db_user_pw: what is the postgrs users pw
    @property
    def db_user_pw(self):
        return self.BASE_DEFAULTS.get("db_user_pw", "admin")

    # db_host: on what host is postgres running
    @property
    def db_host(self):
        return self.BASE_DEFAULTS.get("db_host", "localhost")

    # postgres_port: at what post is postgres running
    @property
    def postgres_port(self):
        return self.BASE_DEFAULTS.get("postgres_port", 5432)

    def __init__(self):
        result_dic = {}
        must_restart = get_config_from_yaml(
            result_dic=result_dic
        )  # will return list of updated configs
        # result_dic will have data from yaml files
        if must_restart:
            print(VALUES_CHANGED % (BASE_PATH, BASE_PATH))
            sys.exit()
        from config.base_info import BASE_DEFAULTS

        self.BASE_DEFAULTS = BASE_DEFAULTS

    # ----------------------------------
    # get_cursor opens a connection to a database
    def get_cursor(self, db_name=None, return_connection=None):
        """
        """
        dbuser = self.db_user
        dbhost = self.db_host
        dbpw = self.db_user_pw
        postgres_port = self.postgres_port
        if not db_name:
            db_name = self.db_name

        if dbpw:
            conn_string = "dbname='%s' user='%s' host='%s' password='%s'" % (
                db_name,
                dbuser,
                dbhost,
                dbpw,
            )
        else:
            conn_string = "dbname='%s' user=%s host='%s'" % (db_name, dbuser, dbhost)
        try:
            conn = psycopg2.connect(conn_string)
        except psycopg2.OperationalError:
            try:
                if postgres_port:
                    conn_string += " port=%s" % postgres_port
                    conn = psycopg2.connect(conn_string)
            except psycopg2.OperationalError:
                print(ERP_NOT_RUNNING % db_name)
                return
        except:
            return

        cursor_d = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if return_connection:
            return cursor_d, conn
        return cursor_d

    def get_odoo(self, no_db=False, verbose=False, login=[], force=False):
        if not self._odoo or login or force:
            """
            get_module_obj logs into odoo and then
            returns an object with which we can manage the list of modules
            bail out if we can not log into a running odoo site

            """
            verbose = verbose or self.opts.verbose
            db_name = self.db_name
            rpchost = self.rpc_host
            rpcport = self.rpc_port
            if login:
                rpcuser = login[0]
            else:
                rpcuser = self.rpc_user
            if login:
                rpcpw = login[1]
            else:
                rpcpw = self.rpc_user_pw
            try:
                import odoorpc
            except ImportError:
                print(bcolors.WARNING + "please install odoorpc")
                print("execute pip install -r install/requirements.txt" + bcolors.ENDC)
                return
            odoo = None
            try:
                if verbose:
                    print("*" * 80)
                    print("about to open connection to:")
                    print("host:%s, port:%s, timeout: %s" % (rpchost, rpcport, 1200))
                if not db_name:
                    print(bcolors.FAIL)
                    print("*" * 80)
                    print("hoppalla no database defined")
                    print(bcolors.ENDC)
                    return
                odoo = odoorpc.ODOO(rpchost, port=rpcport, timeout=1200)
                if not no_db:
                    if verbose:
                        print("about to login:")
                        print(
                            "dbname:%s, rpcuser:%s, rpcpw: %s"
                            % (db_name, rpcuser, rpcpw)
                        )
                        print("*" * 80)
                    try:
                        odoo.login(db_name, rpcuser, rpcpw)
                    except:
                        if verbose:
                            print("login failed, will retry with pw admin:")
                            print(
                                "dbname:%s, rpcuser:%s, rpcpw: admin"
                                % (db_name, rpcuser)
                            )
                            print("*" * 80)
                        odoo.login(db_name, rpcuser, "admin")
            except odoorpc.error.RPCError:
                print(
                    bcolors.FAIL
                    + "could not login to running odoo server host: %s:%s, db: %s, user: %s, pw: %s"
                    % (rpchost, rpcport, db_name, rpcuser, rpcpw)
                    + bcolors.ENDC
                )
                return
            except urllib.error.URLError:
                print(
                    bcolors.FAIL
                    + "could not login to odoo server host: %s:%s, db: %s, user: %s, pw: %s"
                    % (rpchost, rpcport, db_name, rpcuser, rpcpw)
                )
                print("connection was refused")
                print("make sure odoo is running at the given address" + bcolors.ENDC)
                return
            self._odoo = odoo
            if not self._odoo:
                print(
                    bcolors.FAIL
                    + "For what ever reason I could not login to odoo server host: %s:%s, db: %s, user: %s, pw: %s"
                    % (rpchost, rpcport, db_name, rpcuser, rpcpw)
                )
                print("make sure odoo is running at the given address" + bcolors.ENDC)
        if not self._odoo:
            print(ERP_NOT_RUNNING)

        return self._odoo

    def config_setter(self, login=[]):
        """update the config settings for the main company

        Keyword Arguments:
            login {list} -- login and passwird if not actual user (default: {[]})
        """
        from config_settings import c_settings

        odoo = self.get_odoo(login=login)
        if not odoo:
            print(ERP_NOT_RUNNING % self.db_name)
            return
        for object_data in c_settings:
            module = object_data["module"]
            oobjs = odoo.env[module]
            vals_list = object_data["vals_list"]
            key = vals_list[0].get("key")
            if key and oobjs.search([("key", "=", key)]):
                continue
            oobjs.create(vals_list)

    def get_module_obj(self):
        """
            get the ir.module.module
        """
        odoo = self.get_odoo()
        if not odoo:
            return
        module_obj = odoo.env["ir.module.module"]
        return module_obj
