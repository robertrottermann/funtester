#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    # -------- Create: Grade
    "grade": {
        "module": "grade",
        "search": ["name"],  # do not create, when object is found using these elements
        "vals_list": [
            {"active": True, "bfs_grade_code": 25, "name": "Master"},
            {"active": True, "bfs_grade_code": 15, "name": "Bachelor"},
        ],
    },
}