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
                "name": "Spring term 2012",
                "short_name": "FS12",
                "type": "1", #
                "year": 2012,
            },
            {
                "active": True,
                "name": "Summer term 2012",
                "short_name": "SS12",
                "type": "2", # autum
                "year": 2012,
            },
            {
                "active": True,
                "name": "Herbst term 2012",
                "short_name": "HS12",
                "type": "3", # autum
                "year": 2012,
            },
            {
                "active": True,
                "name": "Winter term 2012",
                "short_name": "WS12",
                "type": "4", # autum
                "year": 2012,
            },
            {
                "active": True,
                "name": "Spring term 2013",
                "short_name": "FS13",
                "type": "1", #
                "year": 2013,
            },
            {
                "active": True,
                "name": "Summer term 2013",
                "short_name": "SS13",
                "type": "2", # autum
                "year": 2013,
            },
            {
                "active": True,
                "name": "Herbst term 2013",
                "short_name": "HS13",
                "type": "3", # autum
                "year": 2013,
            },
            {
                "active": True,
                "name": "Winter term 2013",
                "short_name": "WS13",
                "type": "4", # autum
                "year": 2013,
            },
            {
                "active": True,
                "name": "Herbst term 2014",
                "short_name": "HS14",
                "type": "3", # autum
                "year": 2014,
            },
            {
                "active": True,
                "name": "Spring term 2015",
                "short_name": "FS15",
                "type": "1", #
                "year": 2015,
            },
            {
                "active": True,
                "name": "Summer term 2015",
                "short_name": "SS15",
                "type": "2", # autum
                "year": 2015,
            },
            {
                "active": True,
                "name": "Herbst term 2015",
                "short_name": "HS15",
                "type": "3", # autum
                "year": 2015,
            },
            {
                "active": True,
                "name": "Winter term 2015",
                "short_name": "WS15",
                "type": "4", # autum
                "year": 2015,
            },
            {
                "active": True,
                "name": "Spring term 2016",
                "short_name": "FS16",
                "type": "1", # spring
                "year": 2016,
            },
            {
                "active": True,
                "name": "Summer term 2016",
                "short_name": "SS16",
                "type": "2", # summer
                "year": 2016,
            },
            {
                "active": True,
                "name": "Herbst term 2016",
                "short_name": "HS16",
                "type": "3", # autumn
                "year": 2016,
            },
            {
                "active": True,
                "name": "Winter term 2016",
                "short_name": "WS16",
                "type": "4", # winter
                "year": 2016,
            },
            {
                "active": True,
                "name": "Spring term 2017",
                "short_name": "FS17",
                "type": "1", #
                "year": 2017,
            },
            {
                "active": True,
                "name": "Summer term 2017",
                "short_name": "SS17",
                "type": "2", # autum
                "year": 2017,
            },
            {
                "active": True,
                "name": "Herbst term 2017",
                "short_name": "HS17",
                "type": "3", # autum
                "year": 2017,
            },
            {
                "active": True,
                "name": "Winter term 2017",
                "short_name": "WS17",
                "type": "4", # autum
                "year": 2017,
            },            {
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
                "name": "Summersemester 2020",
                "short_name": "SS20",
                "type": "2",  # summer
                "year": 2020,
            },
            {
                "active": True,
                "name": "Herbstsemester 2020",
                "short_name": "HS20",
                "type": "3",  # autumn
                "year": 2020,
            },
            {
                "active": True,
                "name": "Wintersemester 2020",
                "short_name": "WS20",
                "type": "4",  # winter
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
                "name": "Wintersemester 2021",
                "short_name": "WS21",
                "type": "4",  # winter
                "year": 2021,
            },
        ],
    },
}