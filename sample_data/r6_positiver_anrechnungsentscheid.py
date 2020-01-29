#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
"""
Conditions:
studies:
    credit_application_available: True
    remarks_credit_application: "Die zur Anrechnung vorgelegten Leistungen wurden vor mehr als 5 Jahren erarbeitet und entsprechen somit nicht den Voraussetzungen zu einer Anrechnung gemäss Artikel 21 des Studienreglements."

NEEDS:  credit object linked to the studies. See credit.py
        student_semester
        student_module with note credited set

update studies set state_of_study = 'student'  where partner_id=(select id from res_partner where name='Jürgen')
state_of_study:student->registered_1
permission_date:2019-01-23-> ''
decision:permitted->[null]
reason_exmatrikulation:1->[null]
created_email:true->false
created_moodle_account:true->false
guest:[null]->false
remarks_credit_application:''->'hallo velo'
date_remarks_credit_application:[null]->2020-01-28
approval_exmatriculation:true->false
approve_first_section:[null]->false
date_done_credit_module:[null]->2020-01-28
valid_information:true->false
accept_conditions:true->false
approval_exmatriculation_date:2020-01-27->''
kohorte_id:4->[null]
date_start, date_end ??
total_ects_credits:180->0
"""

# ------------------------------------
# sample sample_data
# ------------------------------------
sample_data = {
    # student Jürgen Beer
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
        ],
    },
    "studies": {
        "module": "studies",
        "step": "second_run",
        "search": [
            "partner_id"
        ],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "state_of_study" : 'exmatriculated',
                "abandon": False,
                "regular_student": True,
                "accept_conditions": True,
                "annee_academique": False,
                "approval_exmatriculation": True,
                #"approve_first_section": True,
                "continuing_education": False,
                "created_email": True,
                "created_moodle_account": True,
                "credit_application_available": True,
                "date": False,
                "date_end": ("semester", [("short_name", "FS19")]),
                "date_envoi_diplome": False,
                "date_reception_diplome": False,
                "date_start": ("semester", [("short_name", "FS19")]),
                "decision": 'permitted',
                "diplome": False,
                "disqualification": False,
                "einschreibestatus": False,
                "envoi_va_uni_inscription": False,
                "envoi_va_uni_validation": False,
                "erstsemester": False,
                "exams_failed": False,
                "fachstudiensemester": 0,
                "final_grade": False,
                "finished_immatriculations": True,
                "geburtsort": False,
                "horerstatus": False,
                "kohorte_id": ("kohorte", [("name", "K24")]),
                "missing_documents": False,
                "modules_students": False,
                "motif": False,
                "nom_du_diplome": False,
                "notes": False,
                "part_time": False,
                "partner_id": ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")],),
                "permission_date": '2019-01-23',
                "permission_remark": False,
                "pieces_manquantes_inscription": False,
                "pieces_manquantes_validation": False,
                #"predicate": field is calculated
                "reason_exmatriculation": ("reason.exmatriculation", [("name", "Exmatrikulation auf studentisches Begehren")]),
                "remarks_credit_application": "",
                "remarks_exmatriculation": False,
                "remarques_inscription": False,
                "remarques_validation": False,
                "second_matriculation": False,
                "second_matriculation_branch_study": False,
                "second_matriculation_grade": False,
                "second_matriculation_school_city": False,
                "second_matriculation_school_name": False,
                "second_matriculation_start_study": False,
                "semester": 9,
                "signature_for_study": False,
                "signature_for_study_fname": False,
                'study_course_id': ("study.course", [("study_course_code", "BLAWd")]),
                "study_section_id": ("study.section", [("name", "1. Teil"),('study_course_id', ("study.course", [("study_course_code", "BLAWd")]))]),
                "total_ects_credits": 180,
                "valid_information": True,
                "validation_acquis": False,
            }
        ],
    },
    "study_course": {
        "module": "study.course",
        "search": [
            "study_course_code"
        ],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "access_further_studies_de": False,
                "access_further_studies_en": False,
                "access_further_studies_fr": False,
                "access_requirements_de": False,
                "access_requirements_en": False,
                "access_requirements_fr": False,
                "active": True,
                "additional_documents_online_registration": False,
                "bfs_number": 2505,
                "blocking_semester_ids": [[6, False, []]],
                "canadian_credits": 0,
                "certificate": "Bachelor of Science in Economics",
                "compensation": True,
                "coordination": ("res.partner", [("last_name", "Student Manager"), ("name", "FR")]),
                "cost_center":("account.analytic.account", [("code", "BECOd")]), #1,
                "date_of_introduction_session": False,
                "dekan": ("res.users", [("login", "renate")]),
                "faculty_manager_id": ("res.users", [("login", "petra")]),
                "department_id": ("department", [("name", "Wirtschaftswissenschaften")]),
                "ects": 180,
                "english": False,
                "final_degree_short_name": "B Sc",
                "french": True,
                "german": True,
                "grade_id": ("grade", [("name", "Bachelor")]),
                "guest": False,
                "ignore_sis_import": False,
                "introduction_session_place": False,
                "is_dekansalaryrelevant": True,
                "iuv_group": "I",
                "language_de": True,
                "language_en": False,
                "language_fr": False,
                "level_qualification_de": False,
                "level_qualification_en": False,
                "level_qualification_fr": False,
                "main_de": False,
                "main_en": False,
                "main_fr": False,
                "max_failed_tries": False,
                "max_study_duration": 15,
                "mode_study_de": False,
                "mode_study_en": False,
                "mode_study_fr": False,
                "modules_students": True,
                "moodle_general_courses": False,
                "name": "Bachelor of Science in Economics",
                "offical_length_worlkload_de": False,
                "offical_length_worlkload_en": False,
                "offical_length_worlkload_fr": False,
                "price_application": False,
                "price_holiday": ("product.product", [("default_code", "113")]),
                "price_part_time": ("product.product", [("default_code", "111")]),
                "price_module": ("product.product", [("default_code", "112")]),
                "professional_status_de": False,
                "professional_status_en": False,
                "professional_status_fr": False,
                "programme_requirements_de": False,
                "programme_requirements_en": False,
                "programme_requirements_fr": False,
                "remarks": False,
                "semesters_full_time": 0,
                "semesters_part_time": 9,
                "short_name": "B Sc in Economics",
                "student_resources_type_ids": [[6, False, []]],
                "study_center_id": ("study.center", [("name", "Pfäffikon")]),
                "study_course_code": "BSCECOd",
                "study_course_mail": "studentservices@fernuni.ch",
                "study_course_phone": "0840 840 820",
                "study_course_url": False,
                "study_goal": "Bachelor of Science",
                "subject_study": "Wirtschaftswissenschaft",
                "training_course": False,
                "university_id": ("university", [("name", "Universitäre Fernstudien Schweiz")]),
                "visible_online_registration": True,
                "weiterbildung": False,
                "workgroup_ids": [[6, False, []]],
            },
        ],
    },
}
