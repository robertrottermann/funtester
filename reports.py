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
        'data' : '',
        "condition": """
        object:
        --> ..
        """
    },

}
