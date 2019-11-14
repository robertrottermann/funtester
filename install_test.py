#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A script, that install odoo 13 with some fernuni modules
"""
import os, sys
import urllib.request, urllib.error, urllib.parse
from argparse import ArgumentParser, Namespace
import argparse
import getpass
import psycopg2
import psycopg2.extras

GROUPS = {
        "Student": "fsch_customer.group_fsch_student",
        "Student Reinscription": "fsch_customer.group_fsch_student_reinscription",
        "Mentor / Tutor": "fsch_customer.group_fsch_mentor_tutor",
        "Assist / Dozent": "fsch_customer.group_fsch_assist_dozent",
        "Dekan": "fsch_customer.group_fsch_dekan",
        "Mitarbeiter": "fsch_customer.group_fsch_mitarbeiter",
        "Sekretariat Studieng.": "fsch_customer.group_fsch_sekretariat",
        "SK": "fsch_customer.group_fsch_sk",
        "STZ-Leiter": "fsch_customer.group_fsch_stz_leiter",
        "Manager": "fsch_customer.group_fsch_manager",
        "KST-Leiter": "fsch_customer.group_fsch_kst_leiter",
        "Director": "fsch_customer.group_fsch_director",
        "Barkasse": "fsch_customer.group_fsch_kasse",
        "Revision (Readonly Manager)": "fsch_customer.group_revision",
        "Faculty Manager": "fsch_customer.group_fsch_faculty_manager",
        "Mentorenabrechnungen für Assistenten": "fsch_customer.group_fsch_mentor_allowances_for_assist",
}
USERS = {
    "student": "Student",
    "student_re": "Student Reinscription",
    "tutor": "Mentor / Tutor",
    "dozent": "Assist / Dozent",
    "dekan": "Dekan",
    "mitarbeiter": "Mitarbeiter",
    "sekratariat": "Sekretariat Studieng.",
    "sk": "SK",
    "stzleiter": "STZ-Leiter",
    "manager": "Manager",
    "kstleiter": "KST-Leiter",
    "director": "Director",
    "facultymanager": "Faculty Manager",
    "group_fsch_kasse": "Barkasse",
}
STAFF = {
    "1142": {
        "login": "alexandra",
        "name": "Steiner Alexandra",
        "groups": [
            "fsch_customer.group_fsch_kasse",
            "fsch_customer.group_fsch_kst_leiter",
        ],
    },
    "1140": {
        "login": "matthias",
        "name": "Kubat Matthias",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_faculty_manager",
            "fsch_customer.group_fsch_kst_leiter",
        ],
    },
    "1699": {
        "login": "celine",
        "name": "	Pellissier Céline",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
    },
    "1533": {
        "login": "pedro",
        "name": "Gonzalez Sanchez Pedro Evaristo",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
    },
}
SITE_ADDONS = [
    "crm",
    "stock",
    "account",
    "hr_payroll",
    "hr",
    "hr_expense",
    "board",
    "contacts",
    "hr_holidays",
    "mail",
    "survey",
    "calendar",
]
OWN_ADDONS = ["fsch_customer"]

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


# make sure we are in a virtualenv
# robert: i usualy test in wingide
if not os.environ.get("VIRTUAL_ENV") and not os.environ.get("WINGDB_ACTIVE"):
    print(bcolors.WARNING)
    print("not running in a virtualenv")
    print("activate the worbench environment executing:")
    print("workon workbench or somthing similar")
    print(bcolors.ENDC)
    sys.exit()

try:
    import odoorpc
except ImportError:
    print(bcolors.WARNING + "please install odoorpc")
    print("execute bin/pip install -r install/requirements.txt" + bcolors.ENDC)
    sys.exit()


class MyNamespace(Namespace):
    # we need a namespace that just ignores unknow options
    def __getattr__(self, key):
        if key in self.__dict__.keys():
            return self.__dict__[key]
        return None


class FunidInstaller(object):
    """setup a fernuni installation se we can test it
    This means mostly install some modules and users
    and assign them roles
    """

    db_name = "fernuni13"
    rpc_host = "localhost"
    rpc_port = 8069
    rpc_user = "admin"
    rpc_user_pw = "admin"
    db_user = getpass.getuser()
    db_host = "localhost"
    db_user_pw = "admin"
    postgres_port = 5432

    _odoo = None
    opts = MyNamespace()

    # site_addons is the list of addons provided by odoo
    _site_addons_list = SITE_ADDONS 

    _users = USERS 
    @property
    def users(self):
        return self._users

    _staff = STAFF 
    @property
    def staff(self):
        return self._staff

    _groups = GROUPS
    @property
    def groups(self):
        return self._groups

    # own_addons is the list of addons provided by fernuni or OCA
    _own_addons_list = OWN_ADDONS

    @property
    def site_addons(self):
        return self._site_addons_list

    # _own_addons is the list of addons_entries in the odoo config
    @property
    def own_addons(self):
        return self._own_addons_list

    # ----------------------------------
    #  collects info on what modules are installed
    # or need to be installed
    # @req : list of required modules. If this is an empty list
    #         use any module
    # @uninstalled  : collect unistalled modules into this list
    # @to_upgrade   :collect modules that expect upgrade into this list
    def collect_info(
        self, cursor, req, installed, uninstalled, to_upgrade, all_list=[], apps=[]
    ):
        opts = self.opts
        s = "select * from ir_module_module"
        cursor.execute(s)
        rows = cursor.fetchall()
        all = not req
        updlist = []
        for r in rows:
            n = r.get("name")
            s = r.get("state")
            i = r.get("id")
            if n in req or all:
                if n in req:
                    req.pop(req.index(n))
                if s == "installed":
                    if r.get("application"):
                        apps.append([i, n])
                    if all or updlist == "all" or n in updlist:
                        installed.append((i, n))
                    continue
                elif s in ["uninstalled", "to install"]:
                    uninstalled.append((i, n))
                elif s == "to upgrade":
                    to_upgrade.append(n)
                else:
                    if not s == "uninstallable":
                        print(n, s, i)

    # ----------------------------------
    # get_connection opens a connection to a database
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
            if postgres_port:
                conn_string += " port=%s" % postgres_port
                conn = psycopg2.connect(conn_string)

        cursor_d = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if return_connection:
            return cursor_d, conn
        return cursor_d

    def get_odoo(self, no_db=False, verbose=False):
        if not self._odoo:
            """
            get_module_obj logs into odoo and then
            returns an object with which we can manage the list of modules
            bail out if we can not log into a running odoo site

            """
            verbose = verbose or self.opts.verbose
            db_name = self.db_name
            rpchost = self.rpc_host
            rpcport = self.rpc_port
            rpcuser = self.rpc_user
            rpcpw = self.rpc_user_pw
            try:
                import odoorpc
            except ImportError:
                print(bcolors.WARNING + "please install odoorpc")
                print("execute pip install -r install/requirements.txt" + bcolors.ENDC)
                return
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
                if verbose:
                    return odoo
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
        return self._odoo

    def install_languages(self, languages):
        """
        install all languages in the target
        args:
            languages: list of language codes like ['de_CH, 'fr_CH']

        return:
            dictonary {code : id, ..}
        """
        # what fields do we want to handle?
        # we get the source and target model
        languages = set(languages)
        odoo = self.get_odoo()
        if not odoo:
            print("oddo is not running")
            print("make sure odoo is running at the given address" + bcolors.ENDC)
            return
        langs = odoo.env["base.language.install"]
        result = {}
        lang_obj = odoo.env["res.lang"]
        for code in languages:
            if not langs.search([("lang", "=", code)]):
                # from pdb import set_trace
                # set_trace()
                # odoo.env['ir.translation']._load_module_terms(['base'], [code])
                # #langs.browse(langs.create({'lang': code})).lang_install()
                lang_obj.load_lang(code)
            result[code] = langs.search([("lang", "=", code)])
        return result

    def get_module_obj(self):
        """
            get the ir.module.module
        """
        odoo = self.get_odoo()
        if not odoo:
            return
        module_obj = odoo.env["ir.module.module"]
        return module_obj

    # ----------------------------------
    # install odoo modules
    # or install own modules
    def install_own_modules(self, what="site_addons", quiet=False):
        """
        Install either the odoo apps from site_addons
        or the "own" addons from provided by fernuni/OCA
        """
        module_obj = None
        req = []
        if what == "site_addons":
            # addons decalared in addons are the ones not available from odoo directly
            site_addons = self.site_addons
            req = site_addons
        elif what == "own_addons":
            # addons declared in the own_addons are from fernuni or OCA
            req = self.own_addons

        if req:
            installed = []
            uninstalled = []
            to_upgrade = []

            module_obj = self.get_module_obj()
            if not module_obj:
                # should not happen, means we have no contact to the erp site
                return
            # refresh the list of updatable modules within the erp site
            module_obj.update_list()

            cursor = self.get_cursor()
            self.collect_info(cursor, req, installed, uninstalled, to_upgrade, req[:])
            if req:
                print("*" * 80)
                print("the following modules where not found:", req)
                print("you probably have to download them")
                print("*" * 80)
            if uninstalled:
                print(
                    "the following modules need to be installed:",
                    [u[1] for u in uninstalled],
                )
                i_list = [il[0] for il in uninstalled]
                n_list = [il[1] for il in uninstalled]
                print("*" * 80)
                print(
                    bcolors.OKGREEN + "installing: " + bcolors.ENDC + ",".join(n_list)
                )
                load_demo = False
                if self.opts.single_step or 1:
                    for mname in i_list:
                        module = module_obj.browse([mname])
                        if load_demo:
                            module.demo = True
                        print(
                            "installing:%s%s%s"
                            % (bcolors.OKGREEN, module.name, bcolors.ENDC)
                        )
                        module.button_immediate_install()
                else:
                    modules = module_obj.browse(i_list)
                    if load_demo:
                        for m in modules:
                            m.demo = True
                    modules.button_immediate_install()
                print(
                    bcolors.OKGREEN
                    + "finished installing: "
                    + bcolors.ENDC
                    + ",".join(n_list)
                )
                print("*" * 80)

    mail_outgoing = {
        u"active": True,
        u"name": u"mailhandler@afbs.ch",
        u"sequence": 10,
        u"smtp_debug": False,
        u"smtp_encryption": u"starttls",
        u"smtp_host": u"mail.redcor.ch",
        u"smtp_pass": u"Mailhandler$99",
        u"smtp_port": 25,
        u"smtp_user": u"mailhandler@o2oo.ch",
    }
    mail_incomming = {
        u"active": True,
        u"attach": True,
        u"is_ssl": True,
        u"name": u"mailhandler@afbs.ch",
        u"object_id": False,
        u"original": False,
        u"password": u"Mailhandler$99",
        u"port": 993,
        u"priority": 5,
        # u'script': u'/mail/static/scripts/openerp_mailgate.py',
        u"server": u"mail.redcor.ch",
        u"state": "draft",
        u"server_type": u"imap",
        u"user": u"mailhandler@o2oo.ch",
    }

    def install_mail_handler(self, do_incoming=True):
        # odoo 13, flags when external mailservers are used
        odoo = self.get_odoo()
        res_config_settings = odoo.env["res.config.settings"]
        try:
            try:
                email_setting = res_config_settings.search(
                    [("external_email_server_default", "=", True)]
                )
            except:
                email_setting = []
            odoo.env.ref("base.res_config_settings_view_form").write(
                {"external_email_server_default": True}
            )
            if not email_setting:
                if not email_setting:
                    email_setting = res_config_settings.create(
                        {"external_email_server_default": True}
                    )  # .execute()
                    res_config_settings.external_email_server_default = True
        except:
            pass
        print(bcolors.OKGREEN, "*" * 80)
        if do_incoming:
            # write the incomming email server
            i_server = odoo.env["fetchmail.server"]
            # get the first server
            print("incomming email")
            i_ids = i_server.search([])
            i_id = 0
            i_data = self.mail_incomming
            if i_ids:
                i_id = i_ids[0]
            if i_id:
                incomming = i_server.browse([i_id])
                incomming.write(i_data)
            else:
                incomming = i_server.create(i_data)
            print(i_data)
        print("-" * 80)
        print("outgoing email")
        # now do the same for the outgoing server
        o_data = self.mail_outgoing
        o_server = odoo.env["ir.mail_server"]
        # get the first server
        o_ids = o_server.search([])
        o_id = 0
        if o_ids:
            o_id = o_ids[0]
        if o_id:
            outgoing = o_server.browse([o_id])
            outgoing.write(o_data)
        else:
            o_server.create(o_data)
        print(o_data)
        print("*" * 80, bcolors.ENDC)

    def create_users(self, force=False):
        odoo = self.get_odoo()
        users_o = odoo.env["res.users"]
        users_ox = users_o.with_user(odoo.env.context, 1)
        users = self.users
        groups = self.groups
        # groups_o = odoo.env['res.groups']
        if users:
            for login, user_info in list(users.items()):
                user_data = {}
                user_data["name"] = login
                user_data["email"] = "%s@test.ch" % login
                user_data["login"] = login
                user_data["tz"] = "Europe/Zurich"
                user_data["new_password"] = "login"
                # check if user exists
                user_ids = users_o.search([("login", "=", login)])
                if user_ids:
                    try:
                        user = users_o.browse(user_ids)
                        if force:
                            user.write(user_data)
                    except:
                        pass
                else:
                    # user = odoo.env['res.users'].sudo().with_context().create(user_data)
                    user_id = users_o.create(user_data)
                    if user_id or isinstance(user_id, int):
                        user_ids = [user_id]

                # get groups to be assigned
                group_id = groups[user_info]
                group = odoo.env.ref(group_id)
                group.write({"users": [(4, user_ids[0])]})
        staff = self.staff
        if staff:
            for login, user_info in list(staff.items()):
                u_groups = user_info.pop("groups")
                user_data = user_info
                user_data["email"] = "%s@test.ch" % login
                user_data["tz"] = "Europe/Zurich"
                user_data["new_password"] = "login"
                # check if user exists
                user_ids = users_o.search([("login", "=", user_data['login'])])
                if user_ids:
                    try:
                        user = users_o.browse(user_ids)
                        if force:
                            user.write(user_data)
                    except:
                        pass
                else:
                    # user = odoo.env['res.users'].sudo().with_context().create(user_data)
                    user_id = users_o.create(user_data)
                    if user_id or isinstance(user_id, int):
                        user_ids = [user_id]
                for group_id in u_groups:
                    group = odoo.env.ref(group_id)
                    group.write({"users": [(4, user_ids[0])]})


if __name__ == "__main__":
    installer = FunidInstaller()
    installer.get_odoo(verbose=True)
    print(installer.install_languages(["de_CH", "de_DE", "fr_CH"]))
    installer.install_own_modules()
    installer.install_own_modules(what="own_addons")
    installer.install_mail_handler()
    installer.create_users()
