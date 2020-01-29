#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "student_module" : {
        "step": "second_run",
        "module" : "student.module",
        "search": ['name', 'location_id'],
        "vals_list": [
            {
                'compensation': False,
                'dispensation': False,
                'ignore_asbos': False,
                'message_attachment_count': 0,
                'message_follower_ids': [(0,
                            0,
                            {'partner_id': 2,
                             'res_model': 'student.module',
                             'subtype_ids': [(6, 0, [1])]})],
                'module_data_id': 1,
                'module_without_note': False,
                'moodle_enrollment_created': False,
                'note_credited': True,
                'remark': False,
                'state_student_module': 'open',
                'student_semester_id': (
                    "student.semester", [(
                        "studies_id", ("studies", [("partner_id", ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")]))])
                    )]
                )
            }
        ]
    },
}
