#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "study_section" : {
        "module" : "study.section",
        "search": ["study_course_id", 'number'],
        "vals_list": [
            {
                'active': True,
                'ects_credits': 40,
                'from_semester': 1,
                'name': '1. Teil',
                'to_semester': 2,
                'number': 1,
                'study_course_id': ("study.course", [("study_course_code", "BLAWd")]),
            },
            {
                'active': True,
                'ects_credits': 40,
                'from_semester': 1,
                'name': '1. Teil',
                'to_semester': 2,
                'number': 1,
                'study_course_id': ("study.course", [("study_course_code", "BLAWf")]),
            },
            {
                'active': True,
                'ects_credits': 40,
                'from_semester': 1,
                'name': '1. Teil',
                'to_semester': 2,
                'number': 1,
                'study_course_id': ("study.course", [("study_course_code", "BSCPSYd")]),
            },
            {
                'active': True,
                'ects_credits': 40,
                'from_semester': 1,
                'to_semester': 2,
                'name': 'Propédeutique',
                'number': 1,
                'study_course_id': ("study.course", [("study_course_code", "BSCPSYf")]),
            },
            {
                'active': True,
                'ects_credits': 140,
                'from_semester': 3,
                'to_semester': 9,
                'name': '2ème cycle',
                'number': 2,
                'study_course_id': ("study.course", [("study_course_code", "BSCPSYf")]),
            },
            {
                'active': True,
                'ects_credits': 140,
                'from_semester': 3,
                'to_semester': 9,
                'name': '2ème cycle',
                'number': 2,
                'study_course_id': ("study.course", [("study_course_code", "BSCECOMf")]),
            }
        ]
    },
}