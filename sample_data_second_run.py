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
                "ect_credist": 0,
                "enable_module": False,
                "group": "2",
                "guest": False,
                "kohorte_ids": [[6, False, []]],
                "learning_outcomes": False,
                "message_attachment_count": 0,
                "module_code": False,
                "module_id": 1,
                "module_number": False,
                "modules_students": False,
                "moodle_id": 0,
                "name": "Allgemeine Staatslehre",
                "publish_on_website": False,
                "repetition": "3",
                "requirements": False,
                "semester": False,
                "semester_id": 1,
                "short_name": "Allgemeine Staatslehre",
                # at import time, we do not know yet the values of the study course ids
                # we construct an placehoder value, of which the real value is only set before the second run
                "study_course_ids": [
                    [6, False, get_objects("study.course", login=["matthias", "login"])]
                ],
                "study_section_id": 1,
                "survey_cas_question_ids": [[6, False, []]],
                "survey_specific_question_ids": [[6, False, []]],
                "teaching_material": False,
                "type": False,
                "type_of_exam": "exam",
                "validation_state": "not_validated",
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
