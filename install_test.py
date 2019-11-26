#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""
A script, that installs odoo 13 with some fernuni modules
"""
import os, sys
import urllib.request, urllib.error, urllib.parse
from argparse import Namespace
import getpass
import psycopg2
import psycopg2.extras
from bcolors import bcolors

BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
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
        "last_name": "Steiner",
        "name": "Alexandra",
        "groups": [
            "fsch_customer.group_fsch_kasse",
            "fsch_customer.group_fsch_kst_leiter",
        ],
        # email
        "password": "Login$99",
    },
    "1140": {
        "login": "matthias",
        "last_name": "Kubat",
        "name": "Matthias",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_faculty_manager",
            "fsch_customer.group_fsch_kst_leiter",
            # "fsch_customer.group_fsch_student",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1699": {
        "login": "celine",
        "last_name": "Pellissier",
        "name": "Céline",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1533": {
        "login": "pedro",
        "last_name": "Gonzalez Sanchez",
        "name": "Pedro Evaristo",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
}
MAIL_OUTGOING = {
    u"active": True,
    u"name": u"mailhandler@o2oo.ch",
    u"sequence": 10,
    u"smtp_debug": False,
    u"smtp_encryption": u"starttls",
    u"smtp_host": u"mail.redcor.ch",
    u"smtp_pass": u"Mailhandler$99",
    u"smtp_port": 25,
    u"smtp_user": u"mailhandler@o2oo.ch",
}
MAIL_INCOMMING = {
    u"active": True,
    u"attach": True,
    u"is_ssl": True,
    u"name": u"mailhandler@o2oo.ch",
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
# SITE_ADDONS are the modules that we get from odoo core
SITE_ADDONS = [
    # "crm",
    # "stock",
    # "account",
    # "hr_payroll",
    # "hr",
    # "hr_expense",
    # "board",
    # "contacts",
    # "hr_holidays",
    # "mail",
    # "survey",
    # "calendar",
    # "l10n_ch",
    "base",
    "crm",
    # "crm_voip",  # TODO: v13 migration
    # "bt_report_webkit",  # TODO: v13 migration
    "product",
    # "bt_todo", # TODO: v13 migration
    "hr_payroll",
    "stock",
    "hr_holidays",
    "survey",
    "hr_expense",
    # "l10n_ch_base_bank",
    "analytic",
    # "fsch_pre_migration",  # TODO: v13 migration
    # "account_payment_order",  # TODO: v13 migration
    # "bt_swissdec", # TODO: v13 migration
    # "sett_hr", # TODO: v13 migration
    "board",
    "sale",
    "l10n_ch",
]
# OWN_ADDONS are the modules that we handle our selfs in some
# own (non odoo) repos
OWN_ADDONS = ["fsch_customer"]

# -------------------------------------
# messages
# -------------------------------------
ERP_NOT_RUNNING = """%s------------------------------------------------
Site %%s seems not to run!
------------------------------------------------%s
""" % (
    bcolors.FAIL,
    bcolors.ENDC,
)
VALUES_CHANGED = """%s------------------------------------------------
The config values have changed please check the files in %%s/config/
If wrong please adapt %%s/config.yaml
------------------------------------------------%s
""" % (
    bcolors.WARNING,
    bcolors.ENDC,
)

def get_config_from_yaml(which=['config'], result_dic={}):
    """[read config data from yaml files]
    return dict with config data dicts
    """
    # the base info we need to access the various parts of erp-workbench
    # it is in the config.yaml file in the erp-workbench config folder
    from construct_defaults import check_and_update_base_defaults
    construct_result = {}
    yaml_dic = {}
    for y_info in (
        ("config", "base_info.py"),
    ):
        y_name, file_name = y_info
        if y_name not in which:
            continue
        config_yaml = "%s/%s.yaml" % (BASE_PATH, y_name)
        if not os.path.exists(config_yaml):
            #in_file = "%s.in" % config_yaml
            from shutil import copyfile
            copyfile("%s/%s.yaml.in" % (BASE_PATH, y_name), config_yaml)
        # build a list to be sent to check_and_update_base_defaults
        yaml_dic[y_name] = (
            y_name,
            config_yaml,
            "%s/config/%s" % (BASE_PATH, file_name),
            "%s/%s.yaml.in" % (BASE_PATH, y_name),
        )
        vals = {
            #'USER_HOME' : user_home,
            #'BASE_PATH' : BASE_PATH,
            #'ACT_USER'  : ACT_USER,
            #'DB_USER'   : ACT_USER,
            #'PROJECT_INSTALL': '%(inner_path)s',
            #'SITE_DATA_DIR' : '%(site_data_dir)s',
            #'ERP_VERSION' : '%(erp_version)s',
        }
        # must_reload flags whether we need do restart
        must_reload = check_and_update_base_defaults(
            yaml_dic.values(),
            vals,
            construct_result
        )
        # update the result dic, so the caller can access it 
        result_dic.update(yaml_dic)
        # return dictionary with the values
        return must_reload

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
    print("execute pip install -r requirements.txt" + bcolors.ENDC)
    sys.exit()


class MyNamespace(Namespace):
    # we need a namespace that just ignores unknow options
    def __getattr__(self, key):
        if key in self.__dict__.keys():
            return self.__dict__[key]
        return None


class FunidInstaller(object):
    """setup a fernuni installation so we can test it
    This means mostly install some modules and users
    and assign them roles
    """
    
    BASE_DEFAULTS = {} # will be set when yaml was loaded

    _odoo = None
    opts = MyNamespace()

    # site_addons is the list of addons provided by odoo
    _site_addons_list = SITE_ADDONS
    _mail_outgoing = MAIL_OUTGOING

    @property
    def mail_outgoing(self):
        return self._mail_outgoing

    _mail_incomming = MAIL_INCOMMING

    @property
    def mail_incomming(self):
        return self._mail_incomming

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
    
    # ---------------------------
    # access to odoo and postgres
    # ---------------------------
    @property
    def db_name(self):
        return self.BASE_DEFAULTS.get('db_name', 'fernuni13')
    # rpc_host: on what host is odoo running
    @property
    def rpc_host(self):
        return self.BASE_DEFAULTS.get('rpc_host', '')
    # rpc_port what port is odoo using
    @property
    def rpc_port(self):
        return self.BASE_DEFAULTS.get('rpc_port', 8089)
    # rpc_user: as what user do we access odoo
    @property
    def rpc_user(self):
        return self.BASE_DEFAULTS.get('rpc_user', getpass.getuser())
    # rpc_user_pw: what is the odoo uses pw
    @property
    def rpc_user_pw(self):
        return self.BASE_DEFAULTS.get('rpc_user_pw', 'admin')
    # db_user: as what user are we accessing postgres
    @property
    def db_user(self):
        return self.BASE_DEFAULTS.get('db_user', getpass.getuser())
    # db_user_pw: what is the postgrs users pw
    @property
    def db_user_pw(self):
        return self.BASE_DEFAULTS.get('db_user_pw', 'admin')
    # db_host: on what host is postgres running
    @property
    def db_host(self):
        return self.BASE_DEFAULTS.get('db_host', 'localhost')
    # postgres_port: at what post is postgres running
    @property
    def postgres_port(self):
        return self.BASE_DEFAULTS.get('postgres_port', 5432)
    

    def __init__(self):
        result_dic = {}
        must_restart = get_config_from_yaml(result_dic=result_dic) # will return list of updated configs
                                                                   # result_dic will have data from yaml files
        if must_restart:
            print(VALUES_CHANGED % (BASE_PATH, BASE_PATH))
            sys.exit()
        from config.base_info import BASE_DEFAULTS
        self.BASE_DEFAULTS = BASE_DEFAULTS

    # ----------------------------------
    # collects info on what modules are installed
    # or need to be installed
    # @req : list of required modules. If this is an empty list
    #         use any module
    # @uninstalled  : collect unistalled modules into this list
    # @to_upgrade   :collect modules that expect upgrade into this list
    def collect_info(
        self, cursor, req, installed, uninstalled, to_upgrade, all_list=[], apps=[]
    ):
        #opts = self.opts
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
        else:
            req = what

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

    def install_mail_handler(self, do_incoming=True):
        # odoo 13, flags when external mailservers are used
        # however, it seems not possible to set that flag using odoo_rpc
        odoo = self.get_odoo()
        if not odoo:
            return
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

        companies_o = odoo.env["res.company"]
        companies = companies_o.search([])
        for company in companies:
            c = companies_o.browse([company])
            n = c.email.split("@")[0]
            c.email = "%s@o2oo.ch" % n

    def create_users(self, force=False, strip_fields=[]):
        odoo = self.get_odoo()
        if not odoo:
            return
        users_o = odoo.env["res.users"]
        users_ox = users_o.with_user(odoo.env.context, 1) #???
        users = self.users
        groups = self.groups
        # groups_o = odoo.env['res.groups']
        if users:
            for login, user_info in list(users.items()):
                user_data = {}
                user_data["name"] = login
                user_data["last_name"] = login
                user_data["email"] = "%s@o2oo.ch" % login
                user_data["login"] = login
                user_data["tz"] = "Europe/Zurich"
                user_data["new_password"] = "login"
                # check if user exists
                user_ids = users_o.search([("login", "=", login)])
                for field in strip_fields:
                    user_data.pop(field, None)
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
                user_data["email"] = "%s@o2oo.ch" % login
                user_data["tz"] = "Europe/Zurich"
                user_data["new_password"] = "login"
                # check if user exists
                user_ids = users_o.search([("login", "=", user_data["login"])])
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

    def fixup_partner(self):  # obsolete?
        # fix up demo partner
        # does not really work, odoorpc does not handle sudo or with_user correctly
        # we probably need to use plain odoo RPC
        odoo = self.get_odoo()
        partner_o = odoo.env["res.partner"]
        for partner_id in partner_o.search([]):
            try:
                partner = partner_o.browse([partner_id])
                last = partner.last_name
                email = partner.email
                if not last:
                    print(name, email)
            except:
                print("could not access partner with id: %s" % partner_id)

    def set_passwords(self, password="login", admin="admin"):
        # wrong message!!
        # this sets all password to admin
        installer.get_cursor()
        # create connection
        target_cursor, t_connection = self.get_cursor(return_connection=True)
        t_sql = "UPDATE res_users set password = '%s'"
        t_sql_a = "UPDATE res_users set password = '%s' wher login=admin"
        target_cursor.execute(t_sql % password)
        t_connection.commit()
        print(bcolors.OKGREEN + "*" * 80)
        print("did set all passwords to '%s'" % password)
        if admin != password:
            target_cursor.execute(t_sql % admin)
            t_connection.commit()
            print("did set admin password to '%s' where login='admin'" % admin)
        t_connection.close()
        print("*" * 80 + bcolors.ENDC)


if __name__ == "__main__":
    print(sys.argv)
    db_name = "fernuni13"
    if len(sys.argv) > 1:
        db_name = sys.argv[1]
    installer = FunidInstaller()
    installer.install_own_modules()  # what=['crm'])
    print(installer.install_languages(["de_CH", "de_DE", "fr_CH"]))
    installer.install_own_modules(what="own_addons")
    installer.create_users()  # strip_fields = ['last_name'])
    # installer.install_own_modules()
    installer.install_mail_handler()
    # installer.fixup_partner()
    installer.set_passwords()
