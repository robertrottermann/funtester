#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "module": {
        "module" : "module",
        "search": [
            "module_number", "module_code"
        ],  # do not create, when object is found using these elements
        "vals_list": [
            {
                "active": True,
                # "hide_online": False,
                "lang": "fr_CH",
                "module_code": "SFSD",
                "module_number": "M00",
                "module_visible_report": False,
                "name": "Savoir-faire et savoir devenir",
                "short_name": "Savoir-faire et savoir devenir",
                "study_course_ids": [[6, False, get_objects(
                    "study.course",
                    login=["matthias", "login"],
                    filt=[("study_course_code", "BSCPSYf")]
                )]],
            },
            {
                "active": True,
                # "hide_online": False,
                "lang": "de_DE",
                "module_code": "EINF",
                "module_number": "M01",
                "module_visible_report": False,
                "name": "Einführung in die Psychologie",
                "short_name": "Einführung in die Psychologie",
                "study_course_ids": [[6, False, get_objects("study.course", login=["matthias", "login"])]],
            },
            {
                "active": True,
                # "hide_online": False,
                "lang": "de_DE",
                "module_code": "STAT1",
                "module_number": "M02",
                "module_visible_report": False,
                "name": "Methoden I: Forschungsmethoden und Statistik I",
                "short_name": "Statistik I",
                "study_course_ids": [[6, False, get_objects("study.course", login=["matthias", "login"])]],
            },
            {
                "active": True,
                # "hide_online": False,
                "lang": 'de_DE',
                "module_code": "ENTW",
                "module_number": "M03",
                "module_visible_report": False,
                "name": "Entwicklungspsychologie",
                "short_name": "Entwicklungspsychologie",
                "study_course_ids": [[6, False, get_objects("study.course", login=["matthias", "login"])]],
            },
            {
                "active": True,
                # "hide_online": False,
                "lang": 'de_DE',
                "module_code": "STAAT",
                "module_number": "M03",
                "module_visible_report": False,
                "name": "Allgemeine Staatslehre",
                "short_name": "Allgemeine Staatslehre",
                "study_course_ids": [[6, False, get_objects("study.course", login=["matthias", "login"])]],
            },
            {
                "active": True,
                # "hide_online": False,
                "lang": 'de_DE',
                "module_code": "STAT2",
                "module_number": "M04",
                "module_visible_report": False,
                "name": "Methoden II: Forschungsmethoden und Statistik II",
                "short_name": "Statistik II",
                "study_course_ids": [[6, False, get_objects("study.course", login=["matthias", "login"])]],
            },
            {
                "active": True,
                "hide_online": True,
                "lang": 'fr_CH',
                "module_code": "",
                "module_number": "M18",
                "module_visible_report": False,
                "name": "Travail de Bachelor",
                "short_name": "Travail de Bachelor",
                "study_course_ids": [[6, False,
                    get_objects("study.course", filt=[("study_course_code", '=', "BSCECOMf")], login=["matthias", "login"])]],
            },
        ],
    },
}