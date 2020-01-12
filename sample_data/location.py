#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "location" : {
        "module" : "location",
        "search": ["short_name"],
        "vals_list": [{
            'active': True,
            'address': 'Muesmattstrasse 29, 3012 Bern',
            'location_plan': False,
            'name': 'Pädagogische Hochschule Bern, Institut Sekundarstufe I',
            'responsable_reservation_extern': False,
            'responsable_room_extern': False,
            'short_name': 'PHBE IS1'
        }]
    },
}