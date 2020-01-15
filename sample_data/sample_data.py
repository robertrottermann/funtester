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
    "function",
    "module",
    "module_data",
    "kohorte",
    "location",
    "room",
]
# modules handled in second run
create_sequence_2 = [
    "module_data",
    "kohorte",
    "people",
]
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
    ]
]
from sample_data.first_run import sample_data