#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "event_presence" : {
        "step": "event_list",
        "module" : "event.presence",
        "search": ['studen_module_id', 'event_id'],
        "vals_list": [
            {
                'assigned': False,
                'attended': True,
                'event_id': 1025,
                'login': False,
                'message_attachment_count': 0,
                # 'message_follower_ids': [(0,
                #                             0,
                #                             {'partner_id': 3,
                #                             'res_model': 'event.presence',
                #                             'subtype_ids': [(6, 0, [1])]})],
                'not_attended': False,
                'password': False,
                'studen_module_id': ('student_semester_id', [
                    "student.semester", [(
                        "studies_id", ("studies", [("partner_id", ("res.partner", [("name", "Patrizia"), ("last_name", "Bardola")]))])
                    )]
                ]),

                'students_id': ("partner_id", ("res.partner", [("name", "Patrizia"), ("last_name", "Bardola")])), #52
            }
        ]
    },
}