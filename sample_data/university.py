#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    # -------- creation of university
    "university": {
        "module": "university",
        "search": ["name"],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "active": True,
                "name": "Universitäre Fernstudien Schweiz",
                "price_event_unknown_student_id": (
                    "product.product",
                    [("name", "Teilnahme Präsenzveranstaltung")],
                ),  # 43,
                "pud": False,
                "puf": False,
            }
        ],
    },
}