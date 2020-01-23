#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "works" : {
        "module" : "room",
        "search": [],
        "vals_list": [{
            "name": 'travail de bachelor',
            "date_from": '2018/01/02',
            "date_to": '2018/06/22',
            "remarks": '',
            "finished": 'Finished with payment',
            "studies_id": ("res.partner", [("name", "Eric"), ("last_name", "Tsiroulnikov⁣")],),
            "partner_id": ("res.partner", [("name", "Eric"), ("last_name", "Tsiroulnikov⁣")],),
            "type_id": '',
            "teacher": '',
            "assistant": '',
            "betreuungsvereinbarung": '',
            "digitale_ba_moodle": '',
            "gutachten": '',
            "eigenstandigkeitserklarung": '',
            "compensation_recipient_id": '',
            "ausbezahlt": '2018/05/07/2018',
            "hr_payslip_grosswage_line_id": '',
            "study_course_id": '',
            "student_module_id": '',
            "semester_id": '',
            "module_id": '',
        }]
    },
}
