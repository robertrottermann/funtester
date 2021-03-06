#!/usr/bin/env python
# # -*- coding: utf-8 -*-
"""[summary]
analytic accounts can be access via:
accounting (main selection)->config->analytic accounts-> analytic accounts
"""
from odoo_handler import get_objects
sample_data = {
    # create account.analytic.account
    "account_analytic_account": {
        "module": "account.analytic.account",
        "search": ["code"],
        "login": "admin",
        "vals_list": [
            {
                "active": True,
                "code": "BECOf",
                "company_id": 1,
                "group_id": False,
                "message_attachment_count": 0,
                "message_follower_ids": [
                    (
                        0,
                        0,
                        {
                            "partner_id": get_objects(
                                "res.users",
                                filt=[("login", "celine")],
                                login=['admin', 'admin'],
                                as_list=False,
                                verbose=True),
                            "res_model": "account.analytic.account",
                            "subtype_ids": [(6, 0, [1])],
                        },
                    )
                ],
                "name": "Bachelor Sciences Economiques f",
                "partner_id": False,
            },
            {
                "active": True,
                "code": "BECOd",
                "company_id": 1,
                "group_id": False,
                "message_attachment_count": 0,
                "message_follower_ids": [
                    (
                        0,
                        0,
                        {
                            "partner_id": get_objects(
                                "res.users",
                                filt=[("login", "karin")],
                                login=['admin', 'admin'],
                                as_list=False,
                                verbose=True),
                            "res_model": "account.analytic.account",
                            "subtype_ids": [(6, 0, [1])],
                        },
                    )
                ],
                "name": "Bachelor Wirtschaftswissenschaften d",
                "partner_id": False,
            },
            {
                "active": True,
                "code": "BPSYd",
                "company_id": 1,
                "group_id": False,
                "message_attachment_count": 0,
                "message_follower_ids": [
                    (
                        0,
                        0,
                        {
                            "partner_id": get_objects(
                                "res.users",
                                filt=[("login", "karin")],
                                login=['admin', 'admin'],
                                as_list=False,
                                verbose=True),
                            "res_model": "account.analytic.account",
                            "subtype_ids": [(6, 0, [1])],
                        },
                    )
                ],
                "name": "Bachelor Psychologie d",
                "partner_id": False,
            },
            {
                "active": True,
                "code": "BLAWd",
                "company_id": 1,
                "group_id": False,
                "message_attachment_count": 0,
                "message_follower_ids": [
                    (
                        0,
                        0,
                        {
                            "partner_id": get_objects(
                                "res.users",
                                filt=[("login", "karin")],
                                login=['admin', 'admin'],
                                as_list=False,
                                verbose=True),
                            "res_model": "account.analytic.account",
                            "subtype_ids": [(6, 0, [1])],
                        },
                    )
                ],
                "name": "Bachelor Law d",
                "partner_id": False,
            },
            {
                "active": True,
                "code": "BLAWf",
                "company_id": 1,
                "group_id": False,
                "message_attachment_count": 0,
                "message_follower_ids": [
                    (
                        0,
                        0,
                        {
                            "partner_id": get_objects(
                                "res.users",
                                filt=[("login", "karin")],
                                login=['admin', 'admin'],
                                as_list=False,
                                verbose=True),
                            "res_model": "account.analytic.account",
                            "subtype_ids": [(6, 0, [1])],
                        },
                    )
                ],
                "name": "Bachelor Law f",
                "partner_id": False,
            },
            {
                "active": True,
                "code": "BPSYf",
                "company_id": 1,
                "group_id": False,
                "message_attachment_count": 0,
                "message_follower_ids": [
                    (
                        0,
                        0,
                        {
                            "partner_id": get_objects(
                                "res.users",
                                filt=[("login", "sophie_c")],
                                login=['admin', 'admin'],
                                as_list=False,
                                verbose=True),
                            "res_model": "account.analytic.account",
                            "subtype_ids": [(6, 0, [1])],
                        },
                    )
                ],
                "name": "Bachelor Psychologie f",
                "partner_id": False,
            },
            # when no account exists, and code is used twice
            # we get an error and no account is created
            # or maybe this happens when the user is not yet created ??
            # {
            #     "active": True,
            #     "code": "BLAWd",
            #     "company_id": 1,
            #     "group_id": False,
            #     "message_attachment_count": 0,
            #     "message_follower_ids": [
            #         (
            #             0,
            #             0,
            #             {
            #                 "partner_id": get_objects(
            #                     "res.users",
            #                     filt=[("login", "nicole")],
            #                     login=['admin', 'admin'],
            #                     as_list=False,
            #                     verbose=True),
            #                 "res_model": "account.analytic.account",
            #                 "subtype_ids": [(6, 0, [1])],
            #             },
            #         )
            #     ],
            #     "name": "Bachelor Law d",
            #     "partner_id": False,
            # }
        ],
    },
}