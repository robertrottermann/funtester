#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "event_presence" : {
        "step": "third_run",
        "module" : "event.presence",
        "search": ['studen_module_id', 'event_id'],
        "vals_list": [
            {
                'assigned': False,
                'attended': True,
                'event_id': ('event',
                    [ #1025,
                        ('date', '2019-06-15'),
                        ('type', 'test'),
                        ('module_data_id',
                            (
                                'module.data',
                                [
                                    ("module_code", 'STAAT'),
                                    ("module_number", 'M03'),
                                    ("semester_id", ("semester", [("short_name", "FS20")])),
                                ]
                            )
                        )
                    ]
                ),
                'login': False,
                'message_attachment_count': 0,
                # 'message_follower_ids': [(0,
                #                             0,
                #                             {'partner_id': 3,
                #                             'res_model': 'event.presence',
                #                             'subtype_ids': [(6, 0, [1])]})],
                'not_attended': False,
                'password': False,

                'studen_module_id': ('student.module',
                    [ # list of search domains
                        (
                            "student_semester_id", (
                                "student.semester", [(
                                    "studies_id", ("studies", [("partner_id", ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")]))])
                                )]
                            )
                        ),
                        (
                            'module_data_id', (
                                "module.data", [
                                    ("module_code", 'ARB'),
                                    ("module_number", 'M17'),
                                ]
                            ),
                        )
                    ]
                ),
                'students_id': ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")]), #52
            }
        ]
    },
}