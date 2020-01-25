#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "credit" : {
        "module" : "credit.module",
        "step": "second_run",
        "search": ['studies_id'], #'module_ids'],
        "vals_list": [
            {
                'attachment': True,
                'attachment_fname': False,
                'credit_application': True,
                'credit_records': False,
                'credit_records_filename': False,
                'done': True,
                #'module_ids': [[6, False, [1]]],
                "module_ids": [
                    [6, False, get_objects("module", login=["matthias", "login"], filt=[("module_number", "M01")])]
                ],
                'motivation_letter': False,
                'motivation_letter_filename': False,
                'school_name': 'ETH',
                'studies_id': ("studies", [("partner_id", ("res.partner", [("name", "Martine"), ("last_name", "Freitag")],))]), #3
                # "study_section_id": ("study.section",
                #     [("name", "1. Teil"),('study_course_id', ("study.course", [("study_course_code", "BLAWd")]))]), #1, # SUCHEN!!

            },
            {
                'attachment': True,
                'attachment_fname': False,
                'credit_application': True,
                'credit_records': False,
                'credit_records_filename': False,
                'done': True,
                #'module_ids': [[6, False, [1]]],
                "module_ids": [
                    [6, False, get_objects("module", login=["matthias", "login"], filt=[("module_number", "M01")])]
                ],
                'motivation_letter': False,
                'motivation_letter_filename': False,
                'school_name': 'ETH',
                'studies_id': ("studies", [("partner_id", ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")],))]), #3
                # "study_section_id": ("study.section",
                #     [("name", "1. Teil"),('study_course_id', ("study.course", [("study_course_code", "BLAWd")]))]), #1, # SUCHEN!!

            }
        ]
    },
}