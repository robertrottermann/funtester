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
}