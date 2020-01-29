#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "student_semester" : {
        "step": "second_run",
        "module" : "student.semester",
        "search": ['studies_id', 'semester_id'],
        "vals_list": [
            {
                'choose_student_module_finished': True,
                'date_card_transmitted': '2019-12-30',
                'invoice_id': False,
                'iuv': 'I',
                'part_time': False,
                'remark_dispensation': False,
                'remarks_immatriculation': False,
                'semester_id': ("semester", [("short_name", "FS20")]),
                'state_student_semester': '1',
                'student_module_by_wizard': False,
#                'studies_id': ("studies", 'partner_id', ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")])
                "studies_id": ("studies", [("partner_id", ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")]))]), #1, # SUCHEN!!
                'regular_student': True
            },
        ]
    },
}
