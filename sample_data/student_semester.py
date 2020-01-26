#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "room" : {
        "module" : "room",
        "search": ['name', 'location_id'],
        "vals_list": [
            {
                'choose_student_module_finished': True,
                'date_card_transmitted': '2019-12-30',
                'invoice_id': False,
                'iuv': 'I',
                'part_time': False,
                'remark_dispensation': False,
                'remarks_immatriculation': False,
                'semester_id': 4,
                'state_student_semester': '1',
                'student_module_by_wizard': False,
                'studies_id': 5,
                'regular_student': True
            },
        ]
    },
}
