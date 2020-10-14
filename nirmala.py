#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import odoorpc
import getpass
import psycopg2
import psycopg2.extras
from argparse import Namespace
import urllib.request, urllib.error, urllib.parse


class bcolors:
    """
    allow to colour the bash output
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    white = "\033[1;37m"
    normal = "\033[0;00m"
    red = "\033[1;31m"
    blue = "\033[1;34m"
    green = "\033[1;32m"
    lightblue = "\033[0;34m"

class MyNamespace(Namespace):
    # we need a namespace that just ignores unknow options
    def __getattr__(self, key):
        if key in self.__dict__.keys():
            return self.__dict__[key]
        return None

def get_objects(module, what=["id"], filt=[], login=[], as_list=True, verbose=False):
    """get list of objects of a given type

    Arguments:
        module {string} -- what module to get objects from

    Keyword Arguments:
        what {list} -- which fields to return (default: {['id']})
        filter {list} -- filter to apply to find objects (default: {[]})
        verbose {bool} -- ..
    """
    result = []
    # get_objects might be called in an eval(xxx) situation
    # where we want to use the actual environment with an odoo set
    handler = OdooHandler()
    #if login and login[0] == 'admin':
        #login[0] = 'superadmin'

    odoo = handler.get_odoo(login=login)
    if not odoo:
        return
    env = odoo.env
    m = env[module]
    if filt:
        filt = _construct_filter(filt)
    objs = []
    try:
        objs = m.search(filt)
        if what != ["id"]:
             # if we need more then ids, we must collect
            for obj in m.browse(objs):
                res = ()
                if len(what) > 1:
                    for e in what:
                        res += obj.get(e)
                    result.append(res)
                else:
                    result.append(getattr(obj, what[0]))
        else:
            result = objs
    except odoorpc.error.RPCError as e:
        if verbose:
            print(bcolors.FAIL + "an error occured")
            print(str(e) + bcolors.ENDC)

    if not as_list and result:
        result = result[0]
    if verbose:
        print(module, result)
    return result

def read_image(path=''):
    """read image from fs and make it json serializable

    Keyword Arguments:
        path {str} -- fs path to image (default: {''})

    Returns:
        [type] -- image as encoded string
    """
    data = ''
    img_path = os.path.normpath('%s%s' % (BASE_PATH, path))
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            data = f.read()
    else:
        print('image not found:%s' % img_path)
    return base64.encodebytes(data).decode("utf-8")

class OdooHandler(object):
    BASE_DEFAULTS = {}  # will be set when yaml was loaded

    _odoo = None
    opts = MyNamespace()
    # ---------------------------
    # access to odoo and postgres
    # ---------------------------
    @property
    def db_name(self):
        return self.BASE_DEFAULTS.get("db_name", "redo2oo13")

    # rpc_host: on what host is odoo running
    @property
    def rpc_host(self):
        return self.BASE_DEFAULTS.get("rpc_host", "127.0.0.1")

    # rpc_port what port is odoo using
    @property
    def rpc_port(self):
        return self.BASE_DEFAULTS.get("rpc_port", 8089)

    # rpc_user: as what user do we access odoo
    @property
    def rpc_user(self):
        return 'admin'
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

    # def __init__(self, be_loud=False):
    #     pass

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
        print('--------------------->>', conn_string, cursor_d)
        if return_connection:
            return cursor_d, conn
        return cursor_d

    def get_odoo(self, no_db=False, verbose=True, login=[], force=False, simple=False):
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
                #odoo = odoorpc.ODOO(rpchost, port=rpcport, timeout=1200)
                odoo = odoorpc.ODOO('localhost', port=8069, timeout=1200)
                if not no_db:
                    if verbose or self.be_loud:
                        print("about to login:")
                        print(
                            "dbname:%s, rpcuser:%s, rpcpw: %s"
                            % (db_name, rpcuser, rpcpw)
                        )
                        print("*" * 80)
                    try:
                        if rpcuser == 'admin' and not simple:
                            odoo.login_sudo(db_name, rpcuser, rpcpw) #'admin', 'admin')
                        else:
                            odoo.login(db_name, rpcuser, rpcpw)
                    except AttributeError as e:
                        print(bcolors.FAIL)
                        print('*' * 80)
                        print(str(e))
                        print("maybe you need to install roberts fork of odoorpc")
                        print("from: git@github.com:robertrottermann/odoorpc.git")
                        print(bcolors.ENDC)
                    except Exception as e:
                        if verbose:
                            print("login failed, will retry with pw admin:")
                            print(
                                "dbname:%s, rpcuser:%s, rpcpw: admin"
                                % (db_name, rpcuser)
                            )
                            print("*" * 80)
                        odoo.login_sudo(db_name, rpcuser, "admin")
            except odoorpc.error.RPCError as e:
                print(
                    bcolors.FAIL
                    + "could not login to running odoo server host: %s:%s, db: %s, user: %s, pw: %s"
                    % (rpchost, rpcport, db_name, rpcuser, rpcpw)
                    + bcolors.ENDC
                )
                return
            except urllib.error.URLError as e:
                print(
                    bcolors.FAIL
                    + "could not login to odoo server host: %s:%s, db: %s, user: %s, pw: %s"
                    % (rpchost, rpcport, db_name, rpcuser, rpcpw)
                )
                print((str(e)))
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

handler = OdooHandler()
handler.get_cursor()
get_objects('product.product', verbose=True)
odoo = odoorpc.ODOO('localhost', port=8069, timeout=1200)
x=1