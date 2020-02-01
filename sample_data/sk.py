#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import read_image

sample_data = {
    "sk": {
        "step": "dekan_sk",
        "module": "sk",
        "search": ["study_course_id"],
        "vals_list": [
            {
                "date_start": "2011-02-08",
                "date_to": False,
                "function": "Student Coordinator",
                "name": "BartSK",
                "partner_id": ("res.partner", [("name", "Bartlomiej"), ("last_name", "Chrobak")]),
                "signature": read_image('/sample_data/static/signature_marion_hug.jpeg'),
                "signature_fname": "signature_marion_hug.jpeg",
                "study_course_id": '$xx$', # to be rplaced for each study course id
            }
        ],
    }
}