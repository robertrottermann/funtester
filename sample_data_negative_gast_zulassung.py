#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects

# ------------------------------------
# sample sample_data
# ------------------------------------
sample_data = {
    "semester": {
        "module": "semester",
        "search": [
            "year",
            "type",
        ],  # do not create, when object is found using these elements
        # creating a semester()
        "vals_list": [
            {
                "active": True,
                "name": "25+ Zulassungsprüfung",
                "short_name": "2018_25+",
                "type": "12", # Annual 25+
                "year": 2018,
            },
        ]
    },
    "studies": {
        "module": "studies",
        "search": [
            "partner_id"
        ],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "state_of_study" : 'student',
                "abandon": False,
                "accept_conditions": False,
                "annee_academique": False,
                "approval_exmatriculation": False,
                "approve_first_section": False,
                "continuing_education": False,
                "created_email": False,
                "created_moodle_account": False,
                "credit_application_available": False,
                "date": False,
                "date_end": False,
                "date_envoi_diplome": False,
                "date_reception_diplome": False,
                "date_start": ("semester", [("short_name", "2018_25+")]),
                #"decision": 'permitted',
                "decision": 'not_permitted',
                "diplome": False,
                "disqualification": False,
                "einschreibestatus": False,
                "envoi_va_uni_inscription": False,
                "envoi_va_uni_validation": False,
                "erstsemester": False,
                "exams_failed": False,
                "fachstudiensemester": 0,
                "finished_immatriculations": False,
                "geburtsort": False,
                "horerstatus": False,
                "kohorte_id": False,
                "missing_documents": False,
                "modules_students": False,
                "motif": False,
                "nom_du_diplome": False,
                "notes": False,
                "part_time": False,
                "partner_id": (
                    "res.partner",
                    [("name", "Sébastien"), ("last_name", "Ruffieux")],
                ),  # 70,
                "permission_date": '2020-10-10',
                "permission_remark": False,
                "pieces_manquantes_inscription": False,
                "pieces_manquantes_validation": False,
                "reason_exmatriculation": False,
                "remarks_credit_application": False,
                "remarks_exmatriculation": False,
                "remarques_inscription": False,
                "remarques_validation": False,
                "second_matriculation": False,
                "second_matriculation_branch_study": False,
                "second_matriculation_grade": False,
                "second_matriculation_school_city": False,
                "second_matriculation_school_name": False,
                "second_matriculation_start_study": False,
                "signature_for_study": False,
                "signature_for_study_fname": False,
                'study_course_id': ("study.course", [("certificate", "Admission 25+")]),
                "total_ects_credits": 0,
                "valid_information": False,
                "validation_acquis": False,
                "guest": True,

            }
        ],
    },
    "account_analytic_account": {
        "module": "account.analytic.account",
        "search": ["code"],
        "login": "admin",
        "vals_list": [
            {
                "active": True,
                "code": "25+",
                "company_id": 1,
                "group_id": False,
                "message_attachment_count": 0,
                "name": "Admission 25+",
                "partner_id": False,
            },
        ],
    },
    "department": {
        "module": "department",
        "search": ["name"],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "active": True,
                "french": False,
                "german": True,
                "name": "Admission 25+",
                "short_name": "25+f",
            }
        ],
    },
    "grade": {
        "module": "grade",
        "search": ["name"],  # do not create, when object is found using these elements
        "vals_list": [
            {"active": True, "bfs_grade_code": 0, "name": "Programme spéciaux"},
        ],
    },
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
                "__last_update": False,
                "academic_title": False,
                "active": True,
                "additional_info": False,
                "bfs_student_auth_id_code": False,
                "birthdate": "1984-04-17",
                "certification_date_before": 0,
                "city": 'Bossones',
                "gender": "2",
                "lang": "fr_CH",
                "last_name": "Ruffieux",
                "mobile": '078/715.59.20',
                "name": "Sébastien",
                "profession": 'Ai',
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
                "title": 2,
                "student": True,
            },
        ]
    },
    "study_course": {
        "module": "study.course",
        "search": [
            "certificate"
        ],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "active": True,
                "additional_documents_online_registration": False,
                "bfs_number": 0,
                "blocking_semester_ids": [[6, False, []]],
                "canadian_credits": 0,
                "certificate": "Admission 25+",
                "compensation": False,
                "coordination": ("res.users", [("login", "sophie")]),
                "cost_center":("account.analytic.account", [("code", "25+")]), #1,
                "date_of_introduction_session": False,
                "dekan": False,
                "department_id": ("department", [("name", "Admission 25+")]),
                "ects": 180,
                "english": False,
                "final_degree_short_name": "Admission 25+",
                "french": True,
                "german": False,
                "grade_id": ("grade", [("name", "Programme spéciaux")]),
                "guest": True,
                "ignore_sis_import": False,
                "introduction_session_place": False,
                "is_dekansalaryrelevant": False,
                "iuv_group": False,
                "language_de": False,
                "language_en": False,
                "language_fr": False,
                "level_qualification_de": False,
                "level_qualification_en": False,
                "level_qualification_fr": False,
                "main_de": False,
                "main_en": False,
                "main_fr": False,
                "max_failed_tries": False,
                "max_study_duration": 0,
                "mode_study_de": False,
                "mode_study_en": False,
                "mode_study_fr": False,
                "modules_students": True,
                "moodle_general_courses": False,
                "name": "Admission 25+",
                "offical_length_worlkload_de": False,
                "offical_length_worlkload_en": False,
                "offical_length_worlkload_fr": False,
                "price_application": False,
                "price_holiday": False,
                "price_module": False,
                "price_program": False,
                "professional_status_de": False,
                "professional_status_en": False,
                "professional_status_fr": False,
                "programme_requirements_de": False,
                "programme_requirements_en": False,
                "programme_requirements_fr": False,
                "remarks": False,
                "semesters_full_time": 0,
                "semesters_part_time": 1,
                "short_name": "Admission 25+",
                "student_resources_type_ids": [[6, False, []]],
                "study_center_id": ("study.center", [("name", "Sierre")]),
                "study_course_code": "25+f",
                "study_course_mail": "25plus@unidistance.ch",
                "study_course_phone": "0840 840 830",
                "study_course_url": False,
                "study_goal": "Admission 25+",
                "subject_study": "Psychologie",
                "training_course": False,
                "university_id": ("university", [("name", "Universitäre Fernstudien Schweiz")]), 
                "visible_online_registration": True,
                "weiterbildung": False,
                "workgroup_ids": [[6, False, []]],
            }
        ],
    },
}
