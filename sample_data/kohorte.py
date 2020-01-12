#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    # -------- Create: kohorte
    "kohorte": {
        "module": "kohorte",
        "step": "second_run",
        "search": [
            "name",
            "semester_id",
        ],  # do not create, when object is found using these elements
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