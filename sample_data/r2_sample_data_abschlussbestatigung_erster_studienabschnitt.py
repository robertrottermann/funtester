#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects

# ------------------------------------
# sample sample_data
# ------------------------------------
sample_data = {
    # semester created in semester.py
    "module_data": {
        "module": "module.data",
        "search": [
            "short_name",
            "semester_id",
        ],  # do not create, when object is found using these elements
        "step": "second_run",
        "vals_list": [
            #"Travail de Bachelor"
        ],
    },
    "studies": {
        "module": "studies",
        "search": [
            "partner_id"
        ],  # do not create, when object is found using these elements
        "vals_list": [
            # Tsiroulnikov⁣ exmatrikulated
        ],
    },
    "student": {
        "module": "res.partner",
        # creating a student:
        # self ->res.partner()
        "search": [
            "name",
            "last_name",
        ],  # do not create, when object is found using these elements
        "vals_list": [
            # Tsiroulnikov⁣
        ]
    },
}

