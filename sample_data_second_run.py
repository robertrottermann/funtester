#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects

# ------------------------------------
# sample sample_data
# ------------------------------------
sample_data = {
    "module_data": {
        "module": "module.data",
        "search": [
            "short_name",
            "semester_id",
        ],  # do not create, when object is found using these elements
        "step": "second_run",
        "vals_list": [
            {
                "active": True,
                "choose_student_module": False,
                "content_of_study": False,
                "dependency_finished_ids": [[6, False, []]],
                "dependency_ids": [[6, False, []]],
                "description": False,
                "dummy": False,
                "ect_credist": 10,
                "enable_module": False,
                "group": "2",
                "guest": False,
                "kohorte_ids": [[6, False, []]],
                "learning_outcomes": False,
                "message_attachment_count": 0,
                "module_code": 'STAAT',
                "module_id": 1,
                "module_number": 'M03',
                "modules_students": True,
                "moodle_id": 0,
                "name": "Allgemeine Staatslehre",
                "publish_on_website": False,
                "repetition": "3",
                "requirements": False,
                "semester": False,
                "semester_id": ("semester", [("short_name", "FS20")]),
                "short_name": "Allgemeine Staatslehre",
                "study_course_ids": [
                    [6, False, get_objects("study.course", login=["matthias", "login"])]
                ],
                "study_section_id": 1, # SUCHEN!!
                "survey_cas_question_ids": [[6, False, []]],
                "survey_specific_question_ids": [[6, False, []]],
                "teaching_material": False,
                "type": '1', # Wat is that
                "type_of_exam": "exam",
                "validation_state": "not_validated",
                # "main_cost_accounts_ids": [
                #     [6, False, get_objects(
                #         "account.analytic.account",
                #         as_list=False,
                #         filt=[("code", "BPSYd")],
                #         login=["admin", "admin"],
                #         verbose=True
                #     )],
                # ],#"main_cost_accounts_ids"
                # 'main_cost_accounts_ids': [[0,
                #              'virtual_380',
                #              {'account_analytic_account_id': 10,
                #               'percent': 100}]],
            }
        ],
    },
    # -------- Create: kohorte
    "kohorte": {
        "module": "kohorte",
        "step": "second_run",
        "vals_list": [
            {
                "name": "K28",
                "semester_id": ("semester", [("short_name", "HS20")]),
                "study_course_id": (
                    "study.course",
                    [("certificate", "Bachelor of Science in Psychology")],
                ),
            },
            {
                "name": "k25",
                "semester_id": ("semester", [("short_name", "FS19")]),
                "study_course_id": (
                    "study.course",
                    [("certificate", "Bachelor of Science in Psychology")],
                ),
            },
        ],
    },
}
