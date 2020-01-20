#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
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
                "module_id": ("module", [("module_code", "EINF")]), #1,,
                "module_number": 'M03',
                "modules_students": True,
                "moodle_id": 0,
                "name": "Allgemeine Staatslehre",
                "publish_on_website": False,
                "repetition": "3", #spring and autumn semester
                "requirements": False,
                "semester": 1,
                "semester_id": ("semester", [("short_name", "FS20")]),
                "short_name": "Allgemeine Staatslehre",
                "study_course_ids": [
                    [6, False, get_objects("study.course", login=["matthias", "login"])]
                ],
                "study_section_id": ("study.section", [("name", "1. Teil")]), #1, # SUCHEN!!
                "survey_cas_question_ids": [[6, False, []]],
                "survey_specific_question_ids": [[6, False, []]],
                "teaching_material": False,
                "type": '1', # Wat is that pfichtfach
                "type_of_exam": "exam",
                "validation_state": "not_validated",
                "number_of_events_to_visit": "3",
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
            },
            {
                "active": True,
                "choose_student_module": False,
                "content_of_study": False,
                "dependency_finished_ids": [[6, False, []]],
                "dependency_ids": [[6, False, []]],
                "description": False,
                "dummy": False,
                "ect_credist": 6,
                "enable_module": False,
                "group": "2", #	Students from x. Semester
                "guest": False,
                "kohorte_ids": [[6, False, []]],
                "learning_outcomes": False,
                "message_attachment_count": 0,
                "module_code": 'SFSD',
                "module_id": ("module", [("module_code", "STAAT")]), #1,
                "module_number": 'M00',
                "modules_students": True,
                "moodle_id": 0,
                "name": "Savoir-faire et savoir devenir",
                "publish_on_website": False,
                "repetition": "3", # spring and autumn semester
                "requirements": False,
                "semester": 1,
                "semester_id": ("semester", [("short_name", "FS18")]),
                "short_name": "SF & SD",
                "study_course_ids": [
                    [6, False, get_objects("study.course", login=["matthias", "login"])]
                ],
                "study_section_id": ("study.section", [("name", "Propédeutique")]), #1, # SUCHEN!!
                "survey_cas_question_ids": [[6, False, []]],
                "survey_specific_question_ids": [[6, False, []]],
                "teaching_material": False,
                "type": '1', # 1=pflichtfach
                "type_of_exam": "activity",
                "validation_state": "not_validated",
                "number_of_events_to_visit": "3",
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
}