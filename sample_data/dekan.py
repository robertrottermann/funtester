#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import read_image

sample_data = {
    "dekan": {
        "step": "dekan_sk",
        "module": "dekan",
        "search": ["study_course_id"],
        "vals_list": [
            {
                "date_start": "2014-05-06",
                "date_to": False,
                "function": "Dekan",
                "name": "CélineDK",
                "partner_id": 40,
                "signature": read_image('/sample_data/static/signature_marc_bors.jpeg'),
                "signature_fname": "signature_marc_bors.jpeg",
                "study_course_id": '$xx$', # to be rplaced for each study course id
            }
        ],
    }
}
