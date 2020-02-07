#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A script, that installs odoo 13 with some fernuni modules
"""
import os, sys
import copy
import urllib.request, urllib.error, urllib.parse
from argparse import ArgumentParser
from bcolors import bcolors
from odoo_handler import OdooHandler, get_objects, set_exmatriculated
from messages import *
from sample_data.staff import STAFF, ADMINISTRATOR

FUN_COMPANY = {
    "country_id": 43,
    "phone": "044 77 88 920",
    "street": "Überlandstrasse 12",
    "street2": "Postfach 265",
    "zip": "3900",
    "city": "Brig",
}

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
STUDENT_GROUPS = ["fsch_customer.group_fsch_student"]
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
    "dozent": ["teacher", "customer"],
    "tutor": ["function_id", ("function", [("name", "Dozent/in")])],
    # # funktion teacher:
    # # this is a link of a funktion object ot a field function_1
    # [['res_users_study_course', 'res_users_id','study_course_id'],
    #     ['res.partner','name', 'tutor'], ['function','name', 'Dozent/in']]
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
    # "sale_management",
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
    "funid_registration",
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
            languages: list of language codes like ['de_DE, 'fr_CH']

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

    def create_users(self, force=False, strip_fields=[], users={}):
        odoo = self.get_odoo(login=["admin", "admin"], simple=True)
        if not odoo:
            return
        users_o = odoo.env["res.users"]
        partner_o = odoo.env["res.partner"]
        # set flags for contacts belonging to a user
        # partner_o = odoo.env["res.partner"]
        # print(partner_o.search([('name', 'in',['dozent', 'tutor'])]))
        # partners = partner_o.search([])
        # for partner in partners:
        #     try:
        #         p=partner_o.browse([partner])
        #     except Exception as e:
        #         print(e)
        #         continue
        #     print(p.name)
        # [['is_company', '=', True], ['customer', '=', True]]],
        #     {'fields': ['name', 'country_id', 'comment'], 'limit': 5}
        # )
        # for id, name in partners:
        #     print(id, name)
        if not users:
            users = self.users
            groups = self.groups
        else:
            groups = []
        # groups_o = odoo.env['res.groups']
        if users:
            for login, user_info in list(users.items()):
                user_type = user_info
                if isinstance(user_info, str):
                    user_info = {}
                else:
                    user_type = user_info["user_type"]
                user_data = {}
                user_data["name"] = user_info.get("first_name", login)
                user_data["last_name"] = user_info.get("last_name", login)
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
                if "groups" in user_info.keys():
                    group_ids = user_info["groups"]
                else:
                    if not groups:
                        groups = []
                    group_ids = groups.get(
                        user_type, groups
                    )  # if the groups are self.groups (bbb) then its a string
                    if isinstance(group_ids, str):
                        group_ids = [group_ids]
                for group_id in group_ids:
                    if not group_id:
                        continue
                    group = odoo.env.ref(group_id)
                    group.write({"users": [(4, user_ids[0])]})
                if user_ids:
                    for key in list(user_info.keys()):
                        if key in [
                            "name",
                            "last_name",
                            "email",
                            "login",
                            "tz",
                            "new_password",
                            "user_type",
                        ]:
                            continue
                        user_data[key] = user_info[key]
                    try:
                        partner = partner_o.browse([("parent_id", "=", user_ids[0])])
                        partner.write(user_data)
                    except:
                        pass
        staff = self.staff
        if staff:
            for login, user_info in list(staff.items()):
                u_groups = user_info.pop("groups", [])
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
                    print(user_data)
                    user_id = users_o.create(user_data)
                    if user_id or isinstance(user_id, int):
                        user_ids = [user_id]
                for group_id in u_groups:
                    group = odoo.env.ref(group_id)
                    group.write({"users": [(4, user_ids[0])]})
        # do the assignment of groups to admin also
        a_groups = ADMINISTRATOR["groups"]
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
            param = s_item[1]
            if isinstance(param, tuple):
                param = self._get_object(odoo, param)
            if len(s_item) == 3 and s_item[2] =='%':
                filt.append((s_item[0], "like", param+'%'))
            elif len(s_item) == 3 and s_item[2] =='%%':
                filt.append((s_item[0], "like", '%'+param+'%'))
            else:
                filt.append((s_item[0], "=", param))
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

    def create_objects(
        self, which=[], login=[], step="first_run", sample_data={}, opts=None
    ):
        single_step = None
        if opts and opts.single_step:
            single_step = True
        # create fernuni objects
        from sample_data.sample_data import create_sequence, create_sequence_2, create_sequence_3

        # if we are in single object mode, we can not rely on the step
        if not sample_data:
            if opts and opts.single_object:
                if opts.single_object in create_sequence_2:
                    step = "second_run"
            if step == "first_run":
                from sample_data.sample_data import sample_data as sample_data
            elif step == "second_run":
                from sample_data.sample_data_second_run import (
                    sample_data as sample_data,
                )
                create_sequence = create_sequence_2
            elif step == "third_run":
                from sample_data.sample_data_third_run import (
                    sample_data as sample_data,
                )
                create_sequence = create_sequence_3
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
            # which tells us what object type we want to create, default all
            if not which or object_name in which:
                # only create objects according to running step
                if object_data.get("step", "first_run") != step and object_data.get(
                    "step"
                ) not in ("dekan_sk", "event_list"):
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
                # if its sk or dekan we construct a vals_lst entry for each study-course
                if object_data.get("step") == "dekan_sk":
                    study_course_ids = odoo.env["study.course"].search([])
                    vals_list_temp = []
                    for study_course_id in study_course_ids:
                        vv = {}
                        vv.update(vals_list[0])
                        vv["study_course_id"] = study_course_id
                        vals_list_temp.append(vv)
                    vals_list = vals_list_temp
                # for events we get more event data
                if object_data.get("step") == "event_list":
                    vals_list_data = object_data.get("vals_list_events")
                    dates = vals_list_data['dates']
                    modules = vals_list_data['modules']
                    study_course_ids = odoo.env["study.course"].search([])
                    vals_list_temp = []
                    module_o = odoo.env['module']
                    module_data_o = odoo.env['module.data']
                    for study_course_id in study_course_ids:
                        m_counter = 0
                        for module_number, kohorte, module_code in modules:
                            for name, date, time_from, time_to, room_id in dates:
                                try:
                                    m_counter += 1
                                    print(m_counter, module_number, kohorte ,name, date, time_from, time_to, room_id)
                                    # we need to assign the module data to the event
                                    m_tmp = module_o.search([('module_number', 'like', module_number + '%'), ('module_code', '=', module_code)])
                                    if m_tmp:
                                        module_id = m_tmp[0]
                                    else:
                                        continue
                                    m_tmp = module_data_o.search([('module_id', '=', module_id)])
                                    if m_tmp:
                                        module_data_id = m_tmp[0]
                                        print(module_data_id, module_number, module_id)
                                    else:
                                        print(module_number, module_id, "not found")
                                        continue
                                    vv = {}
                                    vv.update(vals_list[0])
                                    vv['name'] = name
                                    vv['date'] = date
                                    vv['time_from'] = time_from
                                    vv['time_to'] = time_to
                                    vv['room_id'] = room_id
                                    vv['module_data_id'] = module_data_id
                                    vv["study_course_ids"] = [[6, False, [study_course_id]]]
                                    if name == 'Prüfung':
                                        vv['type'] = 'test'
                                    vals_list_temp.append(vv)
                                except Exception as e:
                                    print(HOPPALA_AN_ERROR % str(e))
                                    raise
                    vals_list = vals_list_temp
                # do we have a vals_list_data?
                # then vals_list is only a template from which we build the
                # the populated vals_list
                vals_list_data = object_data.get("vals_list_data")
                if vals_list_data:
                    vals_list_temp = []
                    for data_dic in vals_list_data:
                        vv = copy.deepcopy(vals_list[0])
                        vv.update(data_dic)
                        vals_list_temp.append(vv)
                    vals_list = vals_list_temp
                # now we have collected the vals_list
                # create the odoo objects
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
                    all_vals = vals_list
                    if single_step:
                        for vals_list_dic in all_vals:
                            try:
                                oobjs.create([vals_list_dic])
                            except Exception as e:
                                print("--------> could not create object:", object_name)
                                print(HOPPALA_AN_ERROR % str(e))
                                print(vals_list_dic)
                    else:
                        try:
                            oobjs.create(vals_list)
                        except Exception as e:
                            print("--------> could not create object:", object_name)
                            if opts and opts.verbose:
                                print(HOPPALA_AN_ERROR % str(e))
                                print(vals_list)

                if running_odoo:
                    odoo = running_odoo
            if object_name == "student":
                self.create_student_users(data=object_data)

        # we have to set users to the correct state
        # from
        # set_exmatriculated(odoo, student_state_settings)

    def create_student_users(self, data):
        """crete the users  belonging to the students

        Arguments:
            data {list of dics} -- each entry is a student

        find login and and name from data
        get the contact, and create user that points to it
        """
        odoo = self.get_odoo(login=["admin", "admin"])
        partner_o = odoo.env["res.partner"]
        users_o = odoo.env["res.users"]
        for student_data in data["vals_list"]:
            login = (
                student_data.get("login")
                or student_data.get("matriculation_number")
                or student_data.get("name")
            )
            if not login:
                login = student_data.get("matriculation_number") or student_data.get(
                    "name"
                )
            name = student_data.get("name")
            last_name = student_data.get("last_name")
            vals_u = {"login": login, "name": student_data.get("name")}
            contact = partner_o.search(
                [("name", "=", name), ("last_name", "=", last_name)]
            )
            if not contact:
                continue

            # do we have a user
            c_user = users_o.search([("login", "=", login)])
            # if we have a user, check it it is linked to the
            if not c_user:
                vals_u["partner_id"] = contact[0]
                c_user = users_o.create(vals_u)
                c_user = [c_user]
            res = odoo.execute_kw(
                "res.partner",
                "search_read",
                [[("id", "=", contact[0])]],
                {"fields": ["user_id"]},
            )
            # res is something like:
            # [{'id': 9, 'user_id': False}]
            if not res or not res[0].get("user_id"):
                odoo.execute_kw(
                    "res.partner", "write", [[contact[0]], {"user_id": c_user[0]}]
                )

            for group_id in STUDENT_GROUPS:
                group = odoo.env.ref(group_id)
                group.write({"users": [(4, c_user[0])]})

    def set_company(self):
        """set the address of the company
        """
        odoo = self.get_odoo(login=["admin", "admin"], simple=True)
        companies_o = odoo.env["res.company"]
        companies_o.browse(companies_o.search([])[0]).write(FUN_COMPANY)

    # def set_acounts(self):
    #     """set the recieveabl and payable accounts
    #     """
    #     data = {
    #         'property_account_payable_id': 13,
    #         'property_account_receivable_id': 6,
    #     }

    #     odoo = self.get_odoo(login=['admin', 'admin'])
    #     contacts_o = odoo.env['res.partner']
    #     contacts = contacts_o.search([])
    #     for oc in contacts:
    #         partner = ''
    #         try:
    #             partner = contacts_o.browse([oc]]
    #             partner.write(data)
    #         except Exception as e:
    #             if partner:
    #                 print('failed to set accounts for: %s' % partner.name)
    #             else:
    #                 print(str(e))

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

    def link_objects(self, login=[], object_links=[]):
        # link ojects
        if not object_links:
            from sample_data.sample_data import object_links

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
        # import wingdbstub
        reports_list = opts.reports.split(",")
        reports = list_reports(with_details=True)
        if "all" in reports_list:
            reports_list = list(reports.keys())
        for r_name in reports_list:
            # handling the import fully dynamically is too complicated
            # so we do it hardcoded ..
            sd = {}
            data_runner = None
            if r_name == "1":
                from sample_data.r1_sample_data_negative_gast_zulassung import (
                    sample_data as sd_negzuga,
                )

                sd = sd_negzuga
            if r_name == "2":
                from sample_data.r2_sample_data_abschlussbestatigung_erster_studienabschnitt import (
                    sample_data as sd_abschl_first,
                )

                sd = sd_abschl_first
            if r_name == "5":
                from sample_data.r5_negativer_anrechnungsentscheid import (
                    sample_data as sd_abschl_first,
                )

                sd = sd_abschl_first
            if r_name == "6":
                from sample_data.r6_positiver_anrechnungsentscheid import (
                    sample_data as sd_abschl_first,
                )

                sd = sd_abschl_first
            if r_name == "7":
                from sample_data.r7_sample_data_assistant_report import (
                    assistant_users,
                    run_prepare_report,
                )

                data_runner = run_prepare_report
            if r_name == "11":
                from sample_data.r11_diploma_supplement_report import (
                    assistant_users,
                    run_prepare_report,
                )

                data_runner = run_prepare_report

            if data_runner:
                print(bcolors.green)
                print("executing data-runner for:" + reports[r_name]["name"])
                print(bcolors.ENDC)
                data_runner(self)

            if sd:
                print(bcolors.green)
                print("producing data for:" + reports[r_name]["name"])
                print(bcolors.ENDC)
                self.create_objects(opts=opts, sample_data=sd)


def list_reports(with_details=False):
    from reports import reports

    if not with_details:
        return ["l", "all"] + list(reports.keys())
    return reports


def main(opts):
    if opts.set_company:
        installer = FunidInstaller()
        installer.set_company()
        return

    steps = ["all"]
    if opts.steps:
        if not opts.steps == "all":
            steps = opts.steps.split(",")
    if opts.simple:
        steps = ["lang", "modules"]
    if opts.single_object:
        steps = ["objects"]
    if opts.reports:
        steps = ["reports"]

    print(steps)
    installer = FunidInstaller()
    if "all" in steps or "modules" in steps:
        installer.install_own_modules()  # what=['crm'])
    if "all" in steps or "set_company" in steps:
        installer.set_company()  # what=['crm'])
    if "all" in steps or "lang" in steps:
        print(installer.install_languages(["de_DE", "fr_CH"]))
    if "all" in steps or "fernuni" in steps:
        installer.install_own_modules(what="own_addons")
    if "all" in steps or "users" in steps:
        installer.create_users()  # strip_fields = ['last_name'])
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
        installer.create_objects(
            login=["matthias", "login"], step="second_run", opts=opts
        )
    if "all" in steps or "third_run" in steps:
        installer.create_objects(
            login=["matthias", "login"], step="third_run", opts=opts
        )
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
        choices=list_reports(),
        help="create data for the reports, name reports in comma separate list or l,all. l lists the reports available, all handles all",
    )
    parser.add_argument(
        "-sc",
        "--set_company",
        action="store_true",
        dest="set_company",
        help="set the company data",
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
        "-SS",
        "--single_step",
        action="store_true",
        dest="single_step",
        default=False,
        help="Install objects one by one, so that an error in one object does not fail all of them",
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
