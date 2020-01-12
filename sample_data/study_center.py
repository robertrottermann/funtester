#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    # -------->>>>>>>>>>> Missing Create: Cost Center
    # -------- Create: Study Center
    "study_center": {
        "module": "study.center",
        "search": ["name"],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "active": True,
                "address0": False,
                "address1": False,
                "address2": False,
                "address3": False,
                "address4": False,
                "city": "Brig",
                "e_mail": "studentservices@fernuni.ch",
                "name": "Forschung und Entwicklung",
                "phone": "+41 840 840 820",
                "secretary_user_id": False,
                "short_name": "Forschung und Entwicklung",
                "user_id": ("res.users", [("login", "manuela")]),  # 24,
                "webseite": "http://fernuni.ch/ueber-uns/organisation/standorte/pfaeffikon-sz/",
            },
            {
                "active": True,
                "address0": False,
                "address1": False,
                "address2": False,
                "address3": False,
                "address4": False,
                "city": "Pfäffikon",
                "e_mail": "studentservices@fernuni.ch",
                "name": "Pfäffikon",
                "phone": "+41 840 840 820",
                "secretary_user_id": False,
                "short_name": "Pfäffikon",
                "user_id": ("res.users", [("login", "evelyn")]),  # 24,
                "webseite": "http://fernuni.ch/ueber-uns/organisation/standorte/pfaeffikon-sz/",
            },
            {
                "active": True,
                "address0": False,
                "address1": False,
                "address2": False,
                "address3": False,
                "address4": False,
                "city": "Sierre",
                "e_mail": "studentservices@unidistance.ch",
                "name": "Sierre",
                "phone": "+41 840 840 870",
                "secretary_user_id": False,
                "short_name": "Sierre",
                "user_id": ("res.users", [("login", "manuela")]),  # 24,
                "webseite": "http://unidistance.ch/institution/organisation/centres-detudes/sierre/",
            },
        ],
    },
}