#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
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
                "name": "Spring term 2018",
                "short_name": "FS18",
                "type": "1", # spring
                "year": 2018,
            },
            {
                "active": True,
                "name": "Summer term 2018",
                "short_name": "SS18",
                "type": "2", # summer
                "year": 2018,
            },
            {
                "active": True,
                "name": "Herbst term 2018",
                "short_name": "HS18",
                "type": "3", # autum
                "year": 2018,
            },
            {
                "active": True,
                "name": "Winter term 2018",
                "short_name": "WS18",
                "type": "4", # winter
                "year": 2018,
            },
            {
                "active": True,
                "name": "Spring term 2019",
                "short_name": "FS19",
                "type": "1", # spring
                "year": 2019,
            },
            {
                "active": True,
                "name": "Spring term 2020",
                "short_name": "FS20",
                "type": "1", # spring
                "year": 2020,
            },
            {
                "active": True,
                "name": "Spring term 2021",
                "short_name": "FS21",
                "type": "1",  # spring
                "year": 2021,
            },
            {
                "active": True,
                "name": "Summersemester 2020",
                "short_name": "HS20",
                "type": "2",  # summer
                "year": 2020,
                "name": "Herbstsemester 2019",
                "short_name": "HS19",
                "type": "3",  # autumn
                "year": 2019,
            },
            {
                "active": True,
                "name": "Wintersemester 2021",
                "short_name": "WS21",
                "type": "4",  # winter
                "year": 2021,
            },
        ],
    },
}