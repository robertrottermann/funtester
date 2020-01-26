#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "room" : {
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
                'semester_id': 4,xx
                'state_student_semester': '1',
                'student_module_by_wizard': False,
                'studies_id': 5,xx
                'regular_student': True
            },
        ]
    },
}
