#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
"""
make sure, that study for partner is NOT in exmatriculated state
update studies set state_of_study = 'student'  where partner_id=(select id from res_partner where name='Jürgen');
"""
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
            {
                'choose_student_module_finished': True,
                'date_card_transmitted': '2019-12-30',
                'invoice_id': False,
                'invoice_paid': True,
                'iuv': 'I',
                'part_time': False,
                'remark_dispensation': False,
                'remarks_immatriculation': False,
                'semester_id': ("semester", [("short_name", "HS16")]),
                'state_student_semester': '2',
                'student_module_by_wizard': False,
                "studies_id": ("studies", [("partner_id", ("res.partner", [("name", "Martina"), ("last_name", "Fellay")]))]), #1, # SUCHEN!!
                'regular_student': True
            },
        ]
    },
}
