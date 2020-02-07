#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
sample_data = {
    "event" : {
        "step": "event_list",
        "module" : "event",
        "search": ['name', 'location_id'],
        "vals_list": [
            {
                'date': '2019-02-16',
                'date_to': False,
                'description': False,
                'event_absagetext': False,
                'group': False,
                'literature': False,
                'message_attachment_count': 0,
                # 'message_follower_ids': [(0,
                #                             0,
                #                             {'partner_id': 3,
                #                             'res_model': 'event',
                #                             'subtype_ids': [(6, 0, [1])]})],
                'module': False,
                'module_data_id': 1,
                'name': 'Präsenzveranstaltung 1',
                'publish_on_website': True,
                'registration_possible': True,
                'remarks': False,
                'room_id': 1,
                'semester_id': ("semester", [("short_name", "FS19")],),
                'semester_pud_id': False,
                #'speaker_ids': [[6, False, []]],
                'state': 'closed',
                'state2': False,
                'study_center_id': False,
                'study_course_ids': [[6, False, []]],
                'time_from': 10.25,
                'time_to': 13,
                'type': 'presence_event',
                # 'user_id': 2
            },
        ],
        "vals_list_events":  {
            'dates' : [
                # title                    date         start   end room_id
                ['Präsentvaeranstaltung1', '2019-02-16', 10.25, 13, 1],
                ['Präsentvaeranstaltung2', '2019-03-09', 10.25, 13, 1],
                ['Präsentvaeranstaltung3', '2019-03-30', 10.25, 13, 1],
                ['Präsentvaeranstaltung4', '2019-04-27', 10.25, 13, 1],
                ['Präsentvaeranstaltung5', '2019-05-18', 10.25, 13, 1],
                ['Prüfung',                '2019-06-15', 11.25, 13, 1],
            ],
            'modules' : [
                ['M01', 'K25', 'EINF'],
                ['M02', 'K25', 'STAT1'],
                ['M03', 'K24', 'ENTW'],
                ['M04', 'K24', 'STAT2'],
            ]
        }
    },
}