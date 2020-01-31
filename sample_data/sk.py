#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects

sample_data = {
    "sk": {
        "module": "sk",
        "search": ["study_course_id"],
        "vals_list": [
            {
                "date_start": "2011-02-08",
                "date_to": False,
                "function": "Student Coordinator",
                "name": "BartSK",
                "partner_id": ("partner_id", ("res.partner", [("name", "Bartlomiej"), ("last_name", "Chrobak")])),
                "signature": "",
                "signature_fname": "signature_rodrigo_rodriguez.png",
                "study_course_id": 2,
            }
        ],
    }
}
[(
                        "studies_id", ("studies", [("partner_id", ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")]))])
                    )]