#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects

diploma_supplement_users = {
}
diploma_supplement_links = [
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
    print('diploma supplement stuff')
    handler.create_users(users=diploma_supplement_users)
    handler.link_objects(object_links=diploma_supplement_links)

