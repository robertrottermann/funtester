#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "people" : {
        "module" : "people",
        "search": ['module_data_id', 'teacher_asisstant_id'],
        "vals_list": [
            {
                'date_from': False,
                'date_to': False,
                'module_data_id': ("module.data", [("short_name", "Allgemeine Staatslehre")]),
                'percent': 50,
                'teacher_asisstant_id': ("res.partner", [("name", "dozent")]),
                'type': '1',
                'type_is_mentor_wiwi': False
            }
        ]
    },
}