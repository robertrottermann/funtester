#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
# ------------------------------------
# sample sample_data
# ------------------------------------

# -----------------------
# property_account_receivable_id 121000
# property_account_payable_id 211000
#------------------------

# objects need to created in sequence as they migth refere to
# formerly created ones
create_sequence = [
    "student",
    "semester",
    "price_event",
    "university",
    "study_center",
    "grade",
    "reason_exmatriculation",
    "account_analytic_account",
    "department",
    "study_course",
    "study_section",
    "studies",
    "student_semester",
    "student_module",
    "function",
    "works",
    "module",
    "module_data",
    "credit",
    "kohorte",
    "location",
    "room",
    "people",
    "sk",
    "dekan",
    "event",
]
# modules handled in second run
create_sequence_2 = [
    "module_data",
    "kohorte",
    "people",
    "studies",
    "credit",
    "works",
    "student_semester",
    "student_module",
]
event_data = {
    'dates' : [
        # title                    date         start   end room-no
        ['Präsentvaeranstaltung1', '2019-02-16', 10.25, 13, 1],
        ['Präsentvaeranstaltung2', '2019-03-09', 10.25, 13, 1],
        ['Präsentvaeranstaltung3', '2019-03-30', 10.25, 13, 1],
        ['Präsentvaeranstaltung4', '2019-04-27', 10.25, 13, 1],
        ['Präsentvaeranstaltung5', '2019-05-18', 10.25, 13, 1],
        ['Prüfung',                '2019-06-15', 11.25, 13, 1],
    ],
    'modules' : [
        ['M01', 'K25'],
        ['M02', 'K25'],
        ['M03', 'K24'],
        ['M04', 'K24'],
    ]
}
# create_dekan_sk is done in the first run
# object_links links are a list of object pairs that should be linked
# structure of each entry:
# [database, left_side, right_side]
object_links = [
    # kohorte needs user and study course linked
    # fields: res_user_id, study_course_id
    [
        ["res_users_study_course", "res_users_id", "study_course_id"],
        ["res.users", "login", "matthias"],
        ["study.course", "certificate", "Bachelor of Science in Psychology"],
    ],
    [
        ["res_users_study_course", "res_users_id", "study_course_id"],
        ["res.users", "login", "matthias"],
        ["study.course", "study_course_code", "BLAWd"],
    ],
    [
        ["res_users_study_course", "res_users_id", "study_course_id"],
        ["res.users", "login", "matthias"],
        ["study.course", "study_course_code", "BSCPSYbf"],
    ],
    [
        ["res_users_study_course", "res_users_id", "study_course_id"],
        ["res.users", "login", "matthias"],
        ["study.course", "study_course_code", "BLAWf"],
    ],
    [
        ["res_users_study_course", "res_users_id", "study_course_id"],
        ["res.users", "login", "matthias"],
        ["study.course", "study_course_code", "BSCECOd"],
    ],
    [
        ["res_users_study_course", "res_users_id", "study_course_id"],
        ["res.users", "login", "matthias"],
        ["study.course", "study_course_code", "BSCECOMf"],
    ],
    [
        ["res_users_study_course", "res_users_id", "study_course_id"],
        ["res.users", "login", "jean_paul"],
        ["study.course", "study_course_code", "BSCECOMf"],
    ],
    [
        ["res_users_study_course", "res_users_id", "study_course_id"],
        ["res.users", "login", "thierry"],
        ["study.course", "study_course_code", "BSCECOf"],
    ],
    [
        ["res_users_study_course", "res_users_id", "study_course_id"],
        ["res.users", "login", "thierry"],
        ["study.course", "study_course_code", "BSCECOMf"],
    ]
]
student_state_settings = [
    ('Beer', 'Jürgen', 'exmatriculated'),
    ('Fellay', 'Martina', 'exmatriculated'),
]
from sample_data.first_run import sample_data