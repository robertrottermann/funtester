#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects, read_image
sample_data = {
    # -------->>>>>>>>>>> Create: Create: Department
    "department": {
        "module": "department",
        "search": ["name"],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "active": True,
                "faculty_manager_id": ("res.users", [("login", "malin")]),  # 62,
                "french": False,
                "german": True,
                "name": "Rechtswissenschaften",
                "short_name": "LAWd",
                "visibility_registration": True,
                "website_color": "#e80513",
                "department_icon": read_image('/sample_data/static/droit.png'),
                "registration_name": "Recht",
            },
            {
                "active": True,
                "faculty_manager_id": ("res.users", [("login", "nicole")]),
                "french": False,
                "german": True,
                "name": "Psychologie d",
                "short_name": "PSYd",
                "visibility_registration": True,
                "website_color": "#9a007b",
                "department_icon": read_image('/sample_data/static/psychology_f.png'),
                #"registration_name": "Recht",
            },
            {
                "active": True,
                #"faculty_manager_id": ("res.users", [("login", "nicole")]),
                "french": True,
                "german": False,
                "name": "Admission 25+",
                "short_name": "25+f",
                "visibility_registration": True,
                "website_color": "#FFFFFF",
                "department_icon": read_image('/sample_data/static/admission25_pluss.png'),
                #"registration_name": "Recht",
            },
            {
                "active": True,
                #"faculty_manager_id": ("res.users", [("login", "nicole")]),
                "french": False,
                "german": True,
                "name": "25+ Zulassung",
                "short_name": "25+d",
                "visibility_registration": True,
                "website_color": "#FFFFFF",
                "department_icon": read_image('/sample_data/static/admission25_pluss.png'),
                #"registration_name": "Recht",
            },
        ],
    },
}