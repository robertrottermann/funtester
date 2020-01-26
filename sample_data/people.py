#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "people" : {
        "module" : "people",
        "search": ['module_data_id', 'teacher_asisstant_id'],
        "step": "second_run",
        "vals_list": [
            {
                'date_from': False,
                'date_to': False,
                'module_data_id': ("module.data", [("short_name", "Allgemeine Staatslehre")]),
                'percent': 50,
                'teacher_asisstant_id': ("res.partner", [("name", "dozent")]),
                'type': '1', # 1 teacher, 2 assistent
                'type_is_mentor_wiwi': False
            },
            {
                'date_from': False,
                'date_to': False,
                'module_data_id': ("module.data", [("short_name", "Allgemeine Staatslehre")]),
                'percent': 50,
                'teacher_asisstant_id': ("res.partner", [("name", "dozent")]),
                'type': '1',
                'type_is_mentor_wiwi': False
            },
            {
                'date_from': False,
                'date_to': False,
                'module_data_id': ("module.data", [("short_name", "SF & SD")]),
                'percent': 50,
                'teacher_asisstant_id': ("res.partner", [("email", "1118@o2oo.ch")]),
                'type': '1', # teacher
                'type_is_mentor_wiwi': False,
                'semester_id' : ("semester", [("short_name", "FS18")])
            },
            {
                'date_from': False,
                'date_to': False,
                'module_data_id': ("module.data", [("short_name", "SF & SD")]),
                'percent': 50,
                'teacher_asisstant_id': ("res.partner", [("email", "bartlomiej@o2oo.ch")]),
                'type': '2', # assistant
                'type_is_mentor_wiwi': False,
                'semester_id' : ("semester", [("short_name", "FS18")])
            },
            {
                'date_from': False,
                'date_to': False,
                'module_data_id': ("module.data", [("module_code", 'Travail de Bachelor')]),
                'percent': 50,
                'teacher_asisstant_id': ("res.partner", [("email", "1029@o2oo.ch")]), # simon
                'type': '1', # teacher
                'type_is_mentor_wiwi': False,
                'semester_id' : ("semester", [("short_name", "FS18")])
            },
            {
                'date_from': False,
                'date_to': False,
                'module_data_id': ("module.data", [("module_code", 'SFSD')]),
                'percent': 50,
                'teacher_asisstant_id': ("res.partner", [("email", "admin@example.com")]), # simon
                'type': '1', # teacher
                'type_is_mentor_wiwi': False,
                'semester_id' : ("semester", [("short_name", "FS18")])
            }
        ]
    },
}
