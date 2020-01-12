#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
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
            }
        ],
    },
}