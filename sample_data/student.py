#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "student": {
        "module": "res.partner",
        # creating a student:
        # self ->res.partner()
        "search": [
            "name",
            "last_name",
        ],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "academic_title": False,
                "customer_rank" : 1,
                "active": True,
                "additional_info": False,
                "bfs_student_auth_id_code": False,
                "bfs_before_study_id": False,
                "birthdate": "1982-01-01",
                "certification_date_before": 0,
                "city": 'Villigen',
                "gender": "1",
                "lang": "de_DE",
                "last_name": "Beer",
                "mobile": '+41 76 683 18 77',
                "name": "Jürgen",
                "profession": "Arzt",
                "prospect": False,
                "ref": False,
                "remarks_marketing": False,
                "return_certificate": False,
                "sale_warn": "no-message",
                "signature_for_reports": False,
                "signature_for_reports_fname": False,
                "country_id": 43,
                "street": 'Bessersteinblick 1',
                "street2": False,
                "title": 1,
                "student": True,
                "zip" : "8832",
                "matriculation_number": "18-695-098",
                "login": "18-695-098",
                #"groups": ["fsch_customer.group_fsch_student",],
            },
            {
                "__last_update": False,
                "academic_title": False,
                "active": True,
                "additional_info": False,
                "ahv_number": "999.9999.9999.99",
                "assistant": False,
                "bfs_before_study_id": False,
                "bfs_school_code": False,
                "bfs_student_auth_id_code": False,
                "birthdate": "1999-01-05",
                "certification_date_before": 0,
                "city": False,
                "collaborator_ce": False,
                "comment": False,
                "company_id": False,
                "company_name": False,
                "country_at_auth_identification": False,
                "country_id": False,
                "country_now": False,
                "cover_letter": False,
                "cover_letter_fname": False,
                "customer_rank": 0,
                "cv_file": False,
                "cv_file_fname": False,
                "date_marketing": False,
                "diplomas_file": False,
                "diplomas_file_fname": False,
                "employee": False,
                "enable_contact_data": False,
                "expenses_remarks": False,
                "fields_visible": False,
                "first_name_for_reports": False,
                "for_matri_number": False,
                "foreign_school": False,
                "function": False,
                "function2_id": False,
                "function_id": False,
                "gender": "1",
                "id_cas_file": False,
                "id_cas_file_fname": False,
                "identity_card": False,
                "identity_card_fname": False,
                "image_1920": False,
                "inactive_teacher": False,
                "industry_id": False,
                "invoice_warn": "no-message",
                "invoice_with_post": False,
                "is_company": False,
                "lang": "de_DE",
                "last_name": "Fleissig",
                "last_name_for_reports": False,
                "link_cv": False,
                "matriculation_number": False,
                "mentoren_tutoren": False,
                "message_attachment_count": 0,
                "mobile": False,
                "moodle_id": 0,
                "moodle_pending_discharge": False,
                "moodle_pending_enrollment": False,
                "moodle_synced": False,
                "name": "Student",
                "other": False,
                "partner_gid": 0,
                "phone": False,
                "photo1": False,
                "photo2": False,
                "photo3": False,
                "picking_warn": "no-message",
                "profession": False,
                "property_account_payable_id": 13,
                "property_account_position_id": False,
                "property_account_receivable_id": 6,
                "property_payment_term_id": False,
                "property_stock_customer": 5,
                "property_stock_supplier": 4,
                "property_supplier_payment_term_id": False,
                "prospect": False,
                "ref": False,
                "remarks_marketing": False,
                "return_certificate": False,
                "sale_warn": "no-message",
                "signature_for_reports": False,
                "signature_for_reports_fname": False,
                "state_id": False,
                "street": False,
                "street2": False,
                "student": True,
                "student_auth_identification": False,
                "student_auth_identification_fname": False,
                "student_auth_identification_id": False,
                "supplier_rank": 0,
                "teacher": False,
                "testimonial": False,
                "title": False,
                "training_plan": False,
                "training_plan_fname": False,
                "type": "private",
                "unmarried_name": False,
                "user_id": False,
                "vat": False,
                "website": False,
                "work_certificate": False,
                "work_certificate_fname": False,
                "zip": False,
            },
            # second sample set creating student with nearly everything empty
            {
                "__last_update": False,
                "academic_title": False,
                "active": True,
                "additional_info": False,
                "ahv_number": False,
                "assistant": False,
                "bfs_before_study_id": False,
                "bfs_school_code": False,
                "bfs_student_auth_id_code": False,
                "birthdate": False,
                "category_id": [[6, False, []]],
                "certification_date_before": 0,
                "city": False,
                "collaborator_ce": False,
                "comment": False,
                "company_id": False,
                "company_name": False,
                "company_type": "person",
                "country_at_auth_identification": False,
                "country_id": False,
                "country_now": False,
                "cover_letter": False,
                "cover_letter_fname": False,
                "customer_rank": 0,
                "cv_file": False,
                "cv_file_fname": False,
                "date_marketing": False,
                "diplomas_file": False,
                "diplomas_file_fname": False,
                "email": False,
                "employee": False,
                "enable_contact_data": False,
                "expenses_remarks": False,
                "fields_visible": False,
                "first_name_for_reports": False,
                "for_matri_number": False,
                "foreign_school": False,
                "function": False,
                "function2_id": False,
                "function_id": False,
                "gender": False,
                "id_cas_file": False,
                "id_cas_file_fname": False,
                "identity_card": False,
                "identity_card_fname": False,
                "image_1920": False,
                "inactive_teacher": False,
                "industry_id": False,
                "invoice_warn": "no-message",
                "invoice_with_post": False,
                "is_company": False,
                "lang": "en_US",
                "last_name": "Ho",
                "last_name_for_reports": False,
                "link_cv": False,
                "matriculation_number": False,
                "mentoren_tutoren": False,
                "message_attachment_count": 0,
                "mobile": False,
                "moodle_id": 0,
                "moodle_pending_discharge": False,
                "moodle_pending_enrollment": False,
                "moodle_synced": False,
                "name": "Hugo",
                "other": False,
                "parent_id": False,
                "partner_gid": 0,
                "phone": False,
                "photo1": False,
                "photo2": False,
                "photo3": False,
                "picking_warn": "no-message",
                "profession": False,
                "property_account_payable_id": 13,
                "property_account_position_id": False,
                "property_account_receivable_id": 6,
                "property_payment_term_id": False,
                "property_stock_customer": 5,
                "property_stock_supplier": 4,
                "property_supplier_payment_term_id": False,
                "prospect": False,
                "ref": False,
                "remarks_marketing": False,
                "return_certificate": False,
                "sale_warn": "no-message",
                "signature_for_reports": False,
                "signature_for_reports_fname": False,
                "state_id": False,
                "street": False,
                "street2": False,
                "student": True,
                "student_auth_identification": False,
                "student_auth_identification_fname": False,
                "student_auth_identification_id": False,
                "supplier_rank": 0,
                "teacher": False,
                "testimonial": False,
                "title": False,
                "training_plan": False,
                "training_plan_fname": False,
                "type": "private",
                "unmarried_name": False,
                "user_id": False,
                "vat": False,
                "website": False,
                "work_certificate": False,
                "work_certificate_fname": False,
                "zip": False,
            },
            {
                "academic_title": False,
                "customer_rank" : 1,
                "active": True,
                "additional_info": False,
                "bfs_student_auth_id_code": False,
                "bfs_before_study_id": False,
                "birthdate": "1991-08-25",
                "certification_date_before": 0,
                "city": 'Geneva',
                "gender": "1",
                "lang": "fr_CH",
                "last_name": "Tsiroulnikov⁣",
                "mobile": '+41 79 173 78 70',
                "name": "Eric",
                "profession": False,
                "prospect": False,
                "ref": False,
                "remarks_marketing": False,
                "return_certificate": False,
                "sale_warn": "no-message",
                "signature_for_reports": False,
                "signature_for_reports_fname": False,
                "country_id": 43,
                "street": 'Ch. de la Fontaine 3',
                "street2": False,
                "title": 2,
                "student": True,
                "zip" : "1615",
                "matriculation_number": "13-694-997",
            },
            {
                "academic_title": False,
                "customer_rank" : 1,
                "active": True,
                "additional_info": False,
                "bfs_student_auth_id_code": False,
                "bfs_before_study_id": False,
                "birthdate": "1974-04-29",
                "certification_date_before": 0,
                "city": 'Wilen b. Wollerau',
                "gender": "2",
                "lang": "de_DE",
                "last_name": "Freitag",
                "mobile": '+41 43 499 90 89',
                "name": "Martine",
                "profession": False,
                "prospect": False,
                "ref": False,
                "remarks_marketing": False,
                "return_certificate": False,
                "sale_warn": "no-message",
                "signature_for_reports": False,
                "signature_for_reports_fname": False,
                "country_id": 43,
                "street": 'Wilenstrasse 32',
                "street2": False,
                "title": 2,
                "student": True,
                "zip" : "8832",
                "matriculation_number": "93-724-177",
                "unmarried_name": 'Bolleter',
                "login": "93-724-177",
                #"groups": ["fsch_customer.group_fsch_student",],
            },
            # {
            #     "academic_title": False,
            #     "customer_rank" : 1,
            #     "active": True,
            #     "additional_info": False,
            #     "bfs_student_auth_id_code": False,
            #     "bfs_before_study_id": False, #8229, bfs_before_study_id has to be created first
            #     "birthdate": "1982-01-01",
            #     "certification_date_before": 0,
            #     "city": 'Villigen',
            #     "gender": "1",
            #     "lang": "de_DE",
            #     "last_name": "Beer",
            #     "mobile": '+41 76 683 18 77',
            #     "name": "Jürgen",
            #     "profession": "Arzt",
            #     "prospect": False,
            #     "ref": False,
            #     "remarks_marketing": False,
            #     "return_certificate": False,
            #     "sale_warn": "no-message",
            #     "signature_for_reports": False,
            #     "signature_for_reports_fname": False,
            #     "country_id": 43,
            #     "street": 'Bessersteinblick 1',
            #     "street2": False,
            #     "title": 1,
            #     "student": True,
            #     "zip" : "8832",
            #     "matriculation_number": "18-695-098",
            #     "login": "18-695-098",
            #     #"groups": ["fsch_customer.group_fsch_student",],
            # },
            {
                "academic_title": False,
                "customer_rank" : 1,
                "active": True,
                "additional_info": False,
                "ahv_number": "756.1180.1376.18",
                "bfs_student_auth_id_code": False,
                "bfs_before_study_id": False,
                "birthdate": "1968-07-26",
                "certification_date_before": 0,
                "city": 'Grimisuat',
                "gender": "2",
                "lang": "fr_CH",
                "last_name": "Jaquet",
                "mobile": '+41793304156',
                "name": "Laurence",
                "profession": False,
                "prospect": False,
                "ref": False,
                "remarks_marketing": False,
                "return_certificate": False,
                "sale_warn": "no-message",
                "signature_for_reports": False,
                "signature_for_reports_fname": False,
                "country_id": 43,
                "street": 'Rue des Condémines 16',
                "street2": False,
                "title": 2,
                "student": True,
                "zip" : "1971",
                "matriculation_number": "91-312-140",
                "unmarried_name": 'Hitter',
                "login": "91-312-140",
                #"groups": ["fsch_customer.group_fsch_student",],
            },
            {
                "academic_title": False,
                "customer_rank" : 1,
                "active": True,
                "additional_info": False,
                "ahv_number": "756.5867.0251.51",
                "bfs_student_auth_id_code": False,
                "bfs_before_study_id": False, #8229,
                "birthdate": "1986-11-22",
                "certification_date_before": 0,
                "city": 'Sion',
                "gender": "2",
                "lang": "fr_CH",
                "last_name": "Fellay",
                "phone": '+41 27 565 00 46',
                "mobile": '+41 77 445 25 62',
                "name": "Martina",
                "profession": 'Program manager',
                "prospect": False,
                "ref": False,
                "remarks_marketing": False,
                "return_certificate": False,
                "sale_warn": "no-message",
                "signature_for_reports": False,
                "signature_for_reports_fname": False,
                "country_id": 43,
                "street": 'Rue du Chanoine Berchtold 10',
                "street2": False,
                "title": 2,
                "student": True,
                "zip" : "1950",
                "matriculation_number": "07-425-473",
                "unmarried_name": 'Guetl',
                "login": "07-425-473",
                #"groups": ["fsch_customer.group_fsch_student",],
            },
            {
                "academic_title": False,
                "customer_rank" : 1,
                "active": True,
                "additional_info": False,
                "bfs_student_auth_id_code": False,
                "bfs_before_study_id": False, #8229, bfs_before_study_id has to be created first
                "birthdate": "1982-01-01",
                "certification_date_before": 0,
                "gender": "1",
                "lang": "de_DE",
                "last_name": "Woog⁣",
                "mobile": '+41 76 346 89 86',
                "name": "Marc",
                "profession": "Berufsschullehrer",
                "prospect": False,
                "ref": False,
                "remarks_marketing": False,
                "return_certificate": False,
                "sale_warn": "no-message",
                "signature_for_reports": False,
                "signature_for_reports_fname": False,
                "title": 1,
                "student": True,
                "country_id": 43,
                "street": 'Heerenweg 186',
                "street2": False,
                "zip" : "8255",
                "city": 'Schlattingen',
                "email": "mwoogXX@gmx.net",
                "matriculation_number": "91-703-546",
                "login": "191-703-546",
                #"groups": ["fsch_customer.group_fsch_student",],
            },
            {
                "academic_title": False,
                "customer_rank" : 1,
                "active": True,
                "additional_info": False,
                "bfs_student_auth_id_code": False,
                "bfs_before_study_id": False, #8229, bfs_before_study_id has to be created first
                "birthdate": "1982-01-01",
                "certification_date_before": 0,
                "gender": "2",
                "lang": "de_DE",
                "last_name": "Bardola",
                "name": "Patrizia",
                "street": 'Arnikaweg 12',
                "street2": False,
                "zip" : "8050",
                "city": 'Zürich',
                "mobile": '+41 76 581 79 81',
                "email": "p_bardolaXX@hotmail.com",
                "profession": "Bankangestellte/Studentin",
                "prospect": False,
                "ref": False,
                "remarks_marketing": False,
                "return_certificate": False,
                "sale_warn": "no-message",
                "signature_for_reports": False,
                "signature_for_reports_fname": False,
                "title": 3,
                "student": True,
                "country_id": 43,
                "ahv_number": "756.0429.1142.50",
                "matriculation_number": "11-695-640",
                "login": "11-695-640",
                #"groups": ["fsch_customer.group_fsch_student",],
            },
        ],
    },
}