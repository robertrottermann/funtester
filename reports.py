#!/usr/bin/env python
# # -*- coding: utf-8 -*-
reports = {
    '1' : {
        'name' :'Negativer Zulassungschentscheid Gasthörer',
        'data' : 'sample_data_negative_gast_zulassung',
    },
    '2' : {
        'name' :'Abschlussbestätigung 1. Studienabschnitt',
        'data' : 'abschlussbestaetigung_first_section',
    },
    '5' : {
        'name' :'Negativer Anrechnungsentscheid',
        'data' : 'xxx abschlussbestaetigung_first_section',
    },
    '6' : {
        'name' :'Positiver Anrechnungsentscheid',
        'data' : 'yyy abschlussbestaetigung_first_section',
    },
    '7' : {
        'name' :'Assistents report',
        'data' : 'sample_data_assistant_report',
    },
    '8' : {
        'name' :'Beurlaubungsbestätigun',
        #'data' : 'r11_diploma_supplement_report',
        # invoice must be paid
        # status holiday
        # to show button:
        # open student_semester -> debug mode -> Edit View: Form -> create_beurlaubungsbestatigung -> remove invisible
        # <button icon="gtk-print" name="create_beurlaubungsbestatigung" string="Beurlaubungsbestätigung"
        # type="object" attrs="{'invisible':['|','|',('guest','=', True),('invoice_paid','=', False),('state_student_semester','!=', '2')]}"/>

    },
    '9' : {
        'name' :'Definitive Zulassung',
        #'data' : 'r11_diploma_supplement_report',
        # -----------------------------------
        # date_definitely_allowed has to be set:
        # update studies set "date_definitely_allowed"= '2016-04-03';
        # -----------------------------------
    },
    '10' : {
        'name' :'Definitive Aufnahme Gasthörer',
        # student Woog Mar
        # must be student
        # <button colspan="4" icon="fa-print" name="create_definitive_aufnahme_als_gasthorer" string="Definitive Zulassung Gasthörer"
        # type="object" attrs="{'invisible':['|','|','|',('guest','=',False),('permission_date','=',False),'&amp;','&amp;',
        # ('state_of_study','!=','definitely_allowed'),('state_of_study','!=','student'),('state_of_study','!=','exmatriculated'),
        # '|',('university_pud','=',True),('university_puf','=',True)]}"/>
    },
    '11' : {
        'name' :'Diploma Supplement',
        'data' : 'r11_diploma_supplement_report',
    },
    '15' : {
        'name' :'Diploma Supplement',
        'data' : '',
        "condition": """
        <button colspan="4" icon="fa-print" name="create_exmatrikulationsverfugung" string="Exmatrikulationsverfügung" type="object" attrs="{'invisible':
            ['|','|','|','|',('manual_signature','=',False),('guest','=',True),('date_end','=',False),
            ('approval_exmatriculation','=',False),'|',
            ('university_pud','=',True),('university_puf','=',True)]}"/>"""
    },
    '16' : {
        'name' :'Gasthörerzertifikat',
        'data' : '',
        "condition": """
        object: student-module
        <button icon="gtk-print" name="create_gasthorerzertifikat" string="Gasthörerzertifikat" type="object" attrs="{'invisible':['|','|','|',('guest','=',False),('state_student_module','!=','done'),('date_2_approve','=',False),('module_visible_report','=',True) ]}"/>
        """
    },
    '17' : {
        'name' :'Immatrikulationsbestätigung',
        'old': 'https://odootst.fernuni.ch/web#id=18525&view_type=form&model=res.partner&menu_id=3167&action=236',
        'data' : '',
        "condition": """
        object: Student semester
        --> Semester University has to be set for the relative semester
        <button icon="gtk-print" name="create_immatrikulationsbestatigung" string="Immatrikulationsbestätigung" type="object" attrs="{'invisible':['|','|','|',('puf_university', '!=', False),('guest','=', True),('invoice_paid','=', False),('state_student_semester','!=', '1')]}"/>
        """
    },
    '18' : {
        'name' :'Leistungsbestätigung',
        'old' : 'https://odootst.fernuni.ch/web/?debug=#id=35480&view_type=form&model=student.module&menu_id=',
        'data' : '',
        "condition": """
        object: student.module
        --> ..
        """
    },
    '19' : {
        'name' :'Leistungsbestätigung-Work',
        'old' : 'https://odootst.fernuni.ch/web/?debug=#id=35480&view_type=page&title=Student+Module&model=student.module&action_id=438',
        'data' : '',
        "condition": """
        object:
                                    <button icon="gtk-print" name="create_leistungbestatigung_work" string="Leistungsbestätigung" type="object" attrs="{'invisible':['|', '|', '|', ('type_of_exam', '!=', 'activity'), ('approved_date', '=', False), ('new_exams','=',False), ('guest','=',True)]}"/>
        --> ..
        """
    },
    '20' : {
        'name' :'Timetable',
        'data': """
        kohorte can be added when editing module data
        """,
    },
    '21' : {
        'name' :'Notenblatt',
        'old' : 'https://odootst.fernuni.ch/web/?debug=#id=17120&view_type=form&model=res.partner&menu_id=3167&action=236',
        'data' : 'studies',
        "condition": """
                                <button colspan="4" icon="fa-print" name="create_notenblatt_transcript_records" string="Notenblatt" type="object" attrs="{'invisible':['|','|',('guest','=',True),'|',('total_ects_credits','=',False),('total_ects_credits','&lt;=',0),'|',('university_pud','=',True),('university_puf','=',True)]}"/>

        object:
        --> ..
        """
    },
    '26' : {
        'name' :'Praesenzliste',
        'old' : 'https://odootst.fernuni.ch/web/?debug=#id=17120&view_type=form&model=res.partner&menu_id=3167&action=236',
        'data' : 'studies',
        'path' : '/home/robert/projects/fernuni13/fernuni13/fernuni/funid_reporting/report/report_prasenzliste_html.py',
        "condition": """
                                <button colspan="4" icon="fa-print" name="create_notenblatt_transcript_records" string="Notenblatt" type="object" attrs="{'invisible':['|','|',('guest','=',True),'|',('total_ects_credits','=',False),('total_ects_credits','&lt;=',0),'|',('university_pud','=',True),('university_puf','=',True)]}"/>

        object:
        --> ..
        """
    },
    '33' : {
        'name' :'Teilnahmebestätigung Gasthörer',
        'old': 'https://odootst.fernuni.ch/web/?debug=#id=14571&view_type=page&title=Student+Module&model=student.module&action_id=438',
        'data' : '',
        "condition": """
        object:
        --> ..
        """
    },
    '34' : {
        'name' :'Negativer Zulassungsentscheid',
        'old': 'https://odootst.fernuni.ch/web/?debug=#id=26112&view_type=page&title=Studies&model=studies&action_id=234',
        'data' : '',
        "condition": """
<button colspan="4" icon="gtk-print" name="create_unzureichende_zulassungsvoraussetzungen" string="Negativer Zulassungsentscheid" type="object" attrs="{'invisible':['|','|','|','|',('guest','=',True),('permission_date','=',False),('decision','!=','not_permitted'),('missing_documents','=',False),'|',('university_pud','=',True),('university_puf','=',True)]}"/>
        object:
        --> ..
        """
    },
    '35' : {
        'name' :'zahlungsbestaetigung',
        'old': 'https://odootst.fernuni.ch/web/?debug=#id=14571&view_type=page&title=Student+Module&model=student.module&action_id=438',
        'data' : '',
        "condition": """
        <button icon="gtk-print" name="create_zahlungsbestaetigung" string="Zahlungsbestätigung" type="object" attrs="{'invisible':['|','|','|',('puf_university', '!=', False),('guest','=', True),('invoice_really_paid','=', False),('state_student_semester','!=', '1')]}"/>
        object: student_semester
        --> ..
        http://erp-dev.fernuni.ch:8069/web/webclient/home?debug=#id=34943&view_type=page&title=Student+Semester&model=student.semester&action_id=443
        """
    },
    '36' : {
        'name' :'zulassung_puf',
        'old': 'https://odootst.fernuni.ch/web/?debug=#id=34859&view_type=page&title=Student+Semester&model=student.semester&action_id=443',
        'data' : '',
        "condition": """
        object:
        --> ..
        """
    },

}
