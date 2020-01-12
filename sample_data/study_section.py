#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "study_section" : {
        "module" : "study.section",
        "search": ["study_course_id", 'number'],
        "vals_list": [{
            'active': True,
            'ects_credits': 40,
            'from_semester': 1,
            'name': '1. Teil',
            'number': 1,
            'study_course_id': ("study.course", [("certificate", "Bachelor of Science in Psychology")]),
            'to_semester': 2
        }]
    },
}