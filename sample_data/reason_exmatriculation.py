#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    # -------- Create: Reason Exmatriculation
    "reason_exmatriculation": {
        "module": "reason.exmatriculation",
        "search": ["name"],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "calc_predicate_final_grade": False,
                "manual_signature": False,
                "name": "Exmatrikulation auf studentisches Begehren",
                "text": False,
                "text_report": False,
            },
            {
                "calc_predicate_final_grade": True,
                "manual_signature": False,
                "name": "Exmatrikulation bei erfolgreichem Abschluss",
                "text": "Exmatrikulation bei erfolgreichem Abschluss",
                "text_report": "Exmatrikulation bei erfolgreichem Abschluss",
            },
            {
                "calc_predicate_final_grade": False,
                "manual_signature": False,
                "name": "Exmatrikulation auf studentisches Begehren",
                "text": "Exmatrikulation auf studentisches Begehren",
                "text_report": "Exmatrikulation auf studentisches Begehren",
            },
        ],
    },
}