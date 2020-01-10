#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A script, that installs odoo 13 with some fernuni modules
"""
import os, sys
import urllib.request, urllib.error, urllib.parse
from argparse import ArgumentParser
from bcolors import bcolors
from odoo_handler import OdooHandler, get_objects
from messages import *

GROUPS = {
    "prospect": "",
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
    "prospect": "prospect",
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
CONTACTS = {"prospect": "prospect"}
# what flags we set for the contacts created for the users
CONTACT_FLAGS = {
    "prospect": ["prospect", "customer"],
    "mitarbeiter": ["employee", "customer"],
    "student": ["student", "customer"],
    "tutor": ["teacher", "customer"],
    "tutor": ["function_id", ("function", [("name", "Dozent/in")])],
    # # funktion teacher:
    # # this is a link of a funktion object ot a field function_1
    # [['res_users_study_course', 'res_users_id','study_course_id'],
    #     ['res.partner','name', 'tutor'], ['function','name', 'Dozent/in']]
}
ADMINISTRATOR = {
        "groups": [
            "fsch_customer.group_fsch_student",
            "fsch_customer.group_fsch_student_reinscription",
            "fsch_customer.group_fsch_mentor_tutor",
            "fsch_customer.group_fsch_assist_dozent",
            "fsch_customer.group_fsch_dekan",
            "fsch_customer.group_fsch_mitarbeiter",
            "fsch_customer.group_fsch_sekretariat",
            "fsch_customer.group_fsch_sk",
            "fsch_customer.group_fsch_stz_leiter",
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_kst_leiter",
            "fsch_customer.group_fsch_director",
            "fsch_customer.group_fsch_kasse",
            "fsch_customer.group_revision",
            "fsch_customer.group_fsch_faculty_manager",
            "fsch_customer.group_fsch_mentor_allowances_for_assist",
        ],
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
    "1439": {
        "login": "patrizia",
        "last_name": "Reber-Parvex",
        "name": "Patrizia",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1553": {
        "login": "sophie",
        "last_name": "	Margaronis Eggen",
        "name": "Sophie",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1558": {
        "login": "malin",
        "last_name": "De Boni",
        "name": "Malin",
        "groups": [
            "fsch_customer.group_fsch_sekretariat",
            # "fsch_customer.group_fsch_student",
            "fsch_customer.group_fsch_mitarbeiter",
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
    "1147": {
        "login": "evelyn",
        "last_name": "Winter",
        "name": "Evelyn",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1128": {
        "login": "karin",
        "last_name": "Zedan-Saxer",
        "name": "Karin",
        "groups": [
            "fsch_customer.group_fsch_sekretariat",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1153": {
        "login": "nicole",
        "last_name": "Ruffieux",
        "name": "Nicole",
        "groups": [
            "fsch_customer.group_fsch_sekretariat",
            "fsch_customer.group_fsch_mitarbeiter",
            "fsch_customer.group_fsch_assist_dozent",
        ],
        # email
        "password": "Login$99",
    },
    "1195": {
        "login": "manuela",
        "last_name": "Kummer",
        "name": "Manuela",
        "groups": ["fsch_customer.group_fsch_mitarbeiter"],
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
    "stock",
    "survey",
    "hr_payroll",
    "hr_holidays",
    "hr_expense",
    "hr_attendance",
    # "l10n_ch_base_bank",
    # -> "analytic",
    # "fsch_pre_migration",  # TODO: v13 migration
    # "account_payment_order",  # TODO: v13 migration
    # "bt_swissdec", # TODO: v13 migration
    # "sett_hr", # TODO: v13 migration
    "board",
    #"sale_management",
    "l10n_ch",
]
# OWN_ADDONS are the modules that we handle our selfs in some
# own (non odoo) repos
OWN_ADDONS = [
    "fsch_customer",
    "fsch_sso",
    "fsch_accounting",
    "fsch_survey_edudl",
    "funid_report_base",
    "funid_customer",
    "funid_reporting",
    # "funid_registration",
]
# make sure we are in a virtualenv
# robert: i usualy test in wingide
if not os.environ.get("VIRTUAL_ENV") and not os.environ.get("WINGDB_ACTIVE"):
    print(bcolors.WARNING)
    print("not running in a virtualenv")
    print("activate a virtual environment executing:")
    print("workon workbench or something similar")
    print(bcolors.ENDC)
    sys.exit()

try:
    import odoorpc
except ImportError:
    print(bcolors.WARNING + "please install odoorpc")
    print("execute pip install -r requirements.txt" + bcolors.ENDC)
    sys.exit()


class FunidInstaller(OdooHandler):
    """setup a fernuni installation so we can test it
    This means mostly install some modules and users
    and assign them roles
    """

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
        # opts = self.opts
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
        odoo = self.get_odoo(login=["admin", "admin"], simple=True)
        if not odoo:
            return
        users_o = odoo.env["res.users"]
        users_ox = users_o.with_user(odoo.env.context, 1)  # ???
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
                if group_id:
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
        # do the assignment of groups to admin also
        a_groups = ADMINISTRATOR['groups']
        admin = users_o.search([("login", "=", "admin")])
        for group_id in a_groups:
            group = odoo.env.ref(group_id)
            group.write({"users": [(4, admin[0])]})

    def set_passwords(self, password="login", admin="admin"):
        # wrong message!!
        # this sets all password to admin
        # create connection
        try:
            target_cursor, t_connection = self.get_cursor(return_connection=True)
        except TypeError:
            # site is probaly not running
            return
        t_sql = "UPDATE res_users set password = '%s'"
        t_sql_a = "UPDATE res_users set password = '%s' where login='admin' or id=1"
        target_cursor.execute(t_sql % password)
        t_connection.commit()
        print(bcolors.OKGREEN + "*" * 80)
        print("did set all passwords to '%s'" % password)
        if admin != password:
            target_cursor.execute(t_sql_a % admin)
            t_connection.commit()
            print("did set admin password to '%s' where login='admin'" % admin)
        t_connection.close()
        print("*" * 80 + bcolors.ENDC)

    def _get_object(self, odoo, domain_info):
        """
        return id of object looked up using domain_info
        ('product.product', [('name', 'Teilnahme Präsenzveranstaltung')])
        """
        oobjs = odoo.env[domain_info[0]]
        filt = []
        for s_item in domain_info[1]:
            filt.append((s_item[0], "=", s_item[1]))
        result = oobjs.search(filt)
        if result:
            result = result[0]
        if isinstance(result, int):
            return result
        return

    # def _replace_place_holder(self):
    # """before the second run, we have to replace the place_holders we constructed
    # loading the sample data
    # """
    # from tools import DATA_POOL
    # for v_name, val in DATA_POOL.items():
    ## each val is constructed: DATA_POOL[val_name] = {'retval' : retval, 'method' : method}
    # e_str = val['method']
    # params = val['params']
    # globals()[v_name] = eval(e_str)(*params, self=self)

    def create_objects(self, which=[], login=[], step="first_run", sample_data={}, opts=None):
        # create fernuni objects
        from sample_data import create_sequence, create_sequence_2
        # if we are in single object mode, we can not rely on the step
        if not sample_data:
            if opts and opts.single_object:
                if opts.single_object in create_sequence_2:
                    step = "second_run"
            if step == "first_run":
                from sample_data import sample_data
            elif step == "second_run":
                from sample_data_second_run import sample_data
            if opts and opts.single_object:
                create_sequence = [opts.single_object]
        if login:
            odoo = self.get_odoo(login=login)
        else:
            odoo = self.get_odoo()
        if not odoo:
            if login:
                print(ERP_NOT_RUNNING_PW % (self.db_name, login[0], login[1]))
            else:
                print(
                    ERP_NOT_RUNNING_PW % (self.db_name, self.rpc_user, self.rpc_user_pw)
                )
            return
        for object_name in create_sequence:
            object_data = sample_data.get(object_name)
            if not object_data:
                # in the second run most elements of sequence are allready handeled
                continue
            if not which or object_name in which:
                # only create objects according to running step
                if object_data.get("step", "first_run") != step:
                    continue
                print(step, object_name)
                module = object_data["module"]
                running_odoo = None
                use_login = object_data.get("login")
                if use_login:
                    running_odoo = odoo
                    pw = "login"
                    if use_login == "admin":
                        pw = "admin"
                    odoo = self.get_odoo(login=[use_login, pw])
                oobjs = odoo.env[module]
                search = object_data.get("search")
                vals_list = object_data["vals_list"]
                # loock up linked ids
                counter = -1
                for vals_dic in vals_list:
                    counter += 1
                    for k, v in vals_dic.items():
                        if isinstance(v, tuple):
                            new_val = self._get_object(odoo, v)
                            if new_val:
                                vals_dic[k] = new_val
                            else:
                                print(COULD_NOT_FIND_OBJECT % (module, str(v)))
                                vals_list.pop(counter)  # can I do that ??
                if search:
                    new_vals_list = []
                    for c_item in vals_list:
                        # we construct a search
                        filt = []
                        for s_item in search:
                            val = c_item.get(s_item)
                            if not val:
                                # if the filter value is not part of the dataset to create
                                # there is no use to to look for an objekt
                                filt = []
                                break
                            filt.append((s_item, "=", val))
                        if filt:
                            found = oobjs.search(filt)
                            if found:
                                continue
                        # not found, so create it
                        new_vals_list.append(c_item)
                    vals_list = new_vals_list
                if vals_list:
                    try:
                        oobjs.create(vals_list)
                    except Exception as e:
                        print("--------> could not create object:", object_name)
                        if opts and opts.verbose:
                            print(HOPPALA_AN_ERROR % str(e))

                if running_odoo:
                    odoo = running_odoo

    def patch_fernuni(self):
        # create fernuni objects from sample_data.py
        from fernuni_patches import fernuni_patches

        mpath = self.BASE_DEFAULTS.get("fernuni_module_path")
        must_exit = []
        for module, patch_list in fernuni_patches.items():
            for patch in patch_list:
                fpath = "%s/%s/%s" % (mpath, module, patch[0])
                if not os.path.exists(fpath):
                    print(MODULE_NOT_FOUND % (fpath, module))
                    return
                # open the file as text and check whether the patch line is already there
                with open(fpath) as f:
                    f_data = f.read()
                    f.close()
                if f_data.find(patch[1]) > 0:
                    continue
                # add the line
                f_data += "\n%s" % patch[1]
                with open(fpath, "w") as f:
                    f.write(f_data)
                    f.close()
                must_exit.append(module)
            if must_exit:
                print(MODULE_DATA_CHANGED % str(must_exit))
                sys.exit()

    def link_objects(self, login=[]):
        # link ojects
        from sample_data import object_links

        # a link is something like:
        #    database                 left field                        right field
        # [['res_users_study_course', 'res_user_id'                     'study_course_id']
        #                             module      key     value         module         key             value
        #                            ['res.user','login', 'matthias'], ['study.course','certificate', 'Bachelor of Science in Psychology']]
        odoo = self.get_odoo(login=login)
        if not odoo:
            print(ERP_NOT_RUNNING % self.db_name)
            return
        cursor, connection = self.get_cursor(return_connection=True)
        for data_set in object_links:
            # so we first have to collect the fields
            # left field
            l_id = -1
            r_id = -1
            db = data_set[0][0]
            l_field = data_set[0][1]
            r_field = data_set[0][2]
            l_data = data_set[1]
            l_ids = odoo.env[l_data[0]].search([(l_data[1], "=", l_data[2])])
            if l_ids:
                l_id = l_ids[0]
            r_data = data_set[2]
            r_ids = odoo.env[r_data[0]].search([(r_data[1], "=", r_data[2])])
            if r_ids:
                r_id = r_ids[0]
            if l_id > -1 and r_id > -1:
                # construct search to check if link exists
                sql_search = "select * from %s where %s=%s and %s=%s" % (
                    db,
                    l_field,
                    l_id,
                    r_field,
                    r_id,
                )
                cursor.execute(sql_search)
                rows = cursor.fetchall()
                if rows:
                    continue
                # does not exist, create them
                sql_insert = "insert into  %s (%s, %s) values (%s, %s)" % (
                    db,
                    l_field,
                    r_field,
                    l_id,
                    r_id,
                )
                cursor.execute(sql_insert)
                connection.commit()

    def handle_reports_data(self, opts):
        """make sure that the data for a report exists

        Arguments:
            opts {object} -- namespace with selected option
        """
        reports_list = opts.reports.split(',')
        if 'all' in reports_list:
            reports = list_reports(with_details=True)
            for r_name in list(reports.keys()):
                # handling the import fully dynamically is too complicated
                # so we do it hardcoded ..
                sd = {}
                if r_name == 'negzuga':
                    from sample_data_negative_gast_zulassung import sample_data as sd_negzuga
                    sd = sd_negzuga
                print(bcolors.green)
                print('producing data for:' +  reports[r_name]['name'])
                print(bcolors.ENDC)
                self.create_objects(opts=opts, sample_data=sd)



def list_reports(with_details=False):
    from reports import reports
    if not with_details:
        return ['l', 'all'] + list(reports.keys())
    return reports

def main(opts):
    steps = ["all"]
    if opts.steps:
        if not opts.steps == "all":
            steps = opts.steps.split(",")
    if opts.simple:
        steps = ["modules", "lang"]
    if opts.single_object:
        steps = ["objects"]
    if opts.reports:
        steps = ["reports"]

    print(steps)
    installer = FunidInstaller()
    if "all" in steps or "modules" in steps:
        installer.install_own_modules()  # what=['crm'])
    if "all" in steps or "lang" in steps:
        print(installer.install_languages(["de_CH", "de_DE", "fr_CH"]))
    if "all" in steps or "fernuni" in steps:
        installer.install_own_modules(what="own_addons")
    if "all" in steps or "users" in steps:
        installer.create_users()  # strip_fields = ['last_name'])
    # installer.install_own_modules()
    if "all" in steps or "mail" in steps:
        installer.install_mail_handler()
    if "all" in steps or "passwd" in steps:
        installer.set_passwords()
    # if 'all' in steps or 'patches' in steps:
    #     installer.patch_fernuni()
    if "all" in steps or "objects" in steps:
        installer.create_objects(login=["matthias", "login"], opts=opts)
    if "all" in steps or "links" in steps:
        installer.link_objects(login=["matthias", "login"])
    if "all" in steps or "second_run" in steps:
        installer.create_objects(login=["matthias", "login"], step="second_run", opts=opts)
    if "config" in steps:
        installer.config_setter(login=["admin", "admin"])
    if "single_object" in steps:
        installer.config_setter(login=["admin", "admin"])
    if "reports" in steps:
        installer.handle_reports_data(opts=opts)


USAGE = """install_test.py -h for help on usage
Possible steps are:
    modules     # install odoo modules
    fernuni     # install fernuni modules lik fsch_customer
    lang        # install languages
    users       # create users and assign permissions
    mail        # install mailhandler (pointing to one of roberts servers)
    passwd      # set passwords
    objects     # create fernuni objects
    patches     # add patches found in patches.py to the fernuni modules
    links       # link objects -> sample_data.object_links
    second_run  # create objects after links have been created
    config      # apply setting found in config_settings.py. This is not set automatically using all

    by default all steps are run but config!
"""
if __name__ == "__main__":
    usage = USAGE  # "install_test.py -h for help on usage"
    parser = ArgumentParser(usage=usage)
    parser.add_argument(
        "-s",
        "--steps",
        action="store",
        dest="steps",
        default="all",
        help="what steps to process. steps are separated by comma, nospace!. Default all",
    )
    parser.add_argument(
        "-r",
        "--reports",
        action="store",
        dest="reports",
        choices= list_reports(),
        help="create data for the reports, name reports in comma separate list or l,all. l lists the reports available, all handles all",
    )
    parser.add_argument(
        "-ss",
        "--single_object",
        action="store",
        dest="single_object",
        help="only install a single object like studies or semester",
    )
    parser.add_argument(
        "-S",
        "--simple",
        action="store_true",
        dest="simple",
        default=False,
        help="Simple install. Only install odoo-Modules and languages",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        default=False,
        help="be verbose, default = False",
    )
    opts = parser.parse_args()
    main(opts)
