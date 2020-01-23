#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "function": {
        "module": "function",
        "search": ["name"],  # do not create, when object is found using these elements
        "vals_list": [
            {"active": True, "name": "Dozent/in"},
            {"active": True, "name": "Assistent/in"},
            {"active": True, "name": "Faculty Manager"},
            {"active": True, "name": "Leiter/in Student Services"},
            {"active": True, "name": "MA Student Services"},
        ],
    },
}