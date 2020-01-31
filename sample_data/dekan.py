#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects

sample_data = {
    "dekan": {
        "module": "dekan",
        "search": ["study_course_id"],
        "vals_list": [
            {
                "date_start": "2014-05-06",
                "date_to": False,
                "function": "Dekan",
                "name": "CélineDK",
                "partner_id": 40,
                "signature": "",
                "signature_fname": "signature_marc_bors.jpeg",
                "study_course_id": 2,
            }
        ],
    }
}
