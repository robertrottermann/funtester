#!/usr/bin/env python
# # -*- coding: utf-8 -*-
ADMINISTRATOR = {
        "groups": [
            "fsch_customer.group_fsch_student",
            "fsch_customer.group_fsch_student_reinscription",
            "fsch_customer.group_fsch_mentor_tutor",
            "fsch_customer.group_fsch_assist_dozent",
            "fsch_customer.group_fsch_dekan",
            "fsch_customer.group_fsch_mitarbeiter",
            "fsch_customer.group_fsch_sekretariat",
            "fsch_customer.group_fsch_sk",
            "fsch_customer.group_fsch_stz_leiter",
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_kst_leiter",
            "fsch_customer.group_fsch_director",
            "fsch_customer.group_fsch_kasse",
            "fsch_customer.group_revision",
            "fsch_customer.group_fsch_faculty_manager",
            "fsch_customer.group_fsch_mentor_allowances_for_assist",
        ],
}
STAFF = {
    "1024": {
        "login": "thierry",
        "last_name": "Madiès",
        "name": "Thierry",
        "groups": [
            "fsch_customer.group_fsch_assist_dozent",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
     "1029": {
        "login": "simon",
        "last_name": "Schnyder",
        "name": "Simon⁣",
        "groups": [
            "fsch_customer.group_fsch_assist_dozent",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
        'teacher' : True,
        "gender": "male",
        #'function_id': ("function", [("name", "Dozent/in")]),
        'customer_rank': 1,
},
    "1142": {
        "login": "alexandra",
        "last_name": "Steiner",
        "name": "Alexandra",
        "groups": [
            "fsch_customer.group_fsch_kasse",
            "fsch_customer.group_fsch_kst_leiter",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1151": {
        "login": "jean_paul",
        "last_name": "Droz",
        "name": "Jean-Paul",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_kst_leiter",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1439": {
        "login": "patrizia",
        "last_name": "Reber-Parvex",
        "name": "Patrizia",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1552": {
        "login": "1552",
        "last_name": "Student Manager",
        "name": "FR",
        "groups": [
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
        "gender": "female",
        "email": "studentservices@unidistance.ch",
    },
    "1553": {
        "login": "sophie",
        "last_name": "Margaronis Eggen",
        "name": "Sophie",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1558": {
        "login": "malin",
        "last_name": "De Boni",
        "name": "Malin",
        "groups": [
            "fsch_customer.group_fsch_sekretariat",
            # "fsch_customer.group_fsch_student",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1140": {
        "login": "matthias",
        "last_name": "Kubat",
        "name": "Matthias",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_faculty_manager",
            "fsch_customer.group_fsch_kst_leiter",
            # "fsch_customer.group_fsch_student",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1118": {
        "login": "laurence",
        "last_name": "Gagnière",
        "name": "Laurence⁣",
        "groups": [
            "fsch_customer.group_fsch_assist_dozent",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        'employee' : True,
        'teacher' : True,
        # email
        "password": "Login$99",
        "academic_title": "Dr",
        'birthdate': '1978-04-03',
        "email": "laurence.gagniere@xunidistance.ch",
    },
    "1128": {
        "login": "karin",
        "last_name": "Zedan-Saxer",
        "name": "Karin",
        "groups": [
            "fsch_customer.group_fsch_sekretariat",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1147": {
        "login": "evelyn",
        "last_name": "Winter",
        "name": "Evelyn",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    "1153": {
        "login": "nicole",
        "last_name": "Ruffieux",
        "name": "Nicole",
        "groups": [
            "fsch_customer.group_fsch_sekretariat",
            "fsch_customer.group_fsch_mitarbeiter",
            "fsch_customer.group_fsch_assist_dozent",
        ],
        # email
        "password": "Login$99",
    },
    "1195": {
        "login": "manuela",
        "last_name": "Kummer",
        "name": "Manuela",
        "groups": ["fsch_customer.group_fsch_mitarbeiter"],
        # email
        "password": "Login$99",
    },
    "1699": {
        "login": "celine",
        "last_name": "Pellissier",
        "name": "Céline",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
        # email
        "password": "Login$99",
    },
    '1861' : {
        "login": "sophie_c",
        'name' : 'Sophie',
        'last_name' : 'Cottagnoud',
        'lang': 'fr_CH',
        'gender': "female",
        'birthdate': '1992-09-09',
        'groups' : [
            "fsch_customer.group_fsch_mitarbeiter",
            "fsch_customer.group_fsch_manager",
        ],
        'employee' : True,
        'teacher' : False,
        # 'function_id': ("function", [("name", "Faculty Manager")]),
        'customer_rank': 1,
        "ahv_number": "756.0534.0155.27",
        "mobile": "+41 79 580 97 37",
    },
    "1533": {
        "login": "pedro",
        "last_name": "Gonzalez Sanchez",
        "name": "Pedro Evaristo",
        "groups": [
            "fsch_customer.group_fsch_manager",
            "fsch_customer.group_fsch_mitarbeiter",
        ],
         # email
        "password": "Login$99",
    },
}
