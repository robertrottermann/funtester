#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects

presence_list_users = {
}
presence_list_links = [
    # kohorte needs user and study course linked
    # fields: res_user_id, study_course_id
]

def run_prepare_report(handler):
    """create links for diploma supplement report

    Arguments:
        handler {object, odoo-handler instance} -- used to access odoo


    we need a semester_university
        date diploma feier

    """
    print('presence list stuff')
    handler.create_users(users=presence_list_users)
    handler.link_objects(object_links=presence_list_links)

# ------------------------------------
# sample sample_data
# ------------------------------------
sample_data = {
    "semester": {
        "module": "semester",
        "search": [
            "year",
            "type",
        ],  # do not create, when object is found using these elements
        # creating a semester()
        "vals_list": [
            {
                "active": True,
                "name": "25+ Zulassungsprüfung",
                "short_name": "2018_25+",
                "type": "12", # Annual 25+
                "year": 2018,
            },
        ]
    },
}

