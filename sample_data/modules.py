#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "module": {
        "module" : "module",
        "search": [
            "module_number", "module_code"
        ],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "active": True,
                # "hide_online": False,
                "lang": 'de_DE',
                "module_code": "EINF",
                "module_number": "M01",
                "module_visible_report": False,
                "name": "Einführung in die Psychologie",
                "short_name": "Einführung in die Psychologie",
                "study_course_ids": [[6, False, get_objects("study.course", login=["matthias", "login"])]],
            },
            {
                "active": True,
                # "hide_online": False,
                "lang": 'de_DE',
                "module_code": "STAAT",
                "module_number": "M03",
                "module_visible_report": False,
                "name": "Allgemeine Staatslehre",
                "short_name": "Allgemeine Staatslehre",
                "study_course_ids": [[6, False, get_objects("study.course", login=["matthias", "login"])]],
            },
            {
                "active": True,
                "hide_online": True,
                "lang": 'fr_CH',
                "module_code": "",
                "module_number": "M18",
                "module_visible_report": False,
                "name": "Travail de Bachelor",
                "short_name": "Travail de Bachelor",
                "study_course_ids": [[6, False,
                    get_objects("study.course", filt=[("study_course_code", '=', "BSCECOMf")], login=["matthias", "login"])]],
            },
        ],
    },
}