#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "room" : {
        "module" : "room",
        "search": [],
        "vals_list": [{'active': True,
            'location_id': ("location", [("short_name", "PHBE IS1")]),
            'name': 'Hörraum 004',
            'number_seats': 65,
            'remarks': 'Beamer, OHP',
            'room_plan': False,
            'room_plan_fname': False
        }]
    },
}