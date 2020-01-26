#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A script, that installs odoo 13 with some fernuni modules
"""
import os, sys
import urllib.request, urllib.error, urllib.parse
from argparse import ArgumentParser
from bcolors import bcolors
from odoo_handler import OdooHandler, get_objects
from messages import *
from sample_data.staff import STAFF, ADMINISTRATOR

class Play(OdooHandler):
    pass

p=Play(1)
odoo=p.get_odoo()
res = odoo.execute_kw(
    'res.partner', 'search_read',
    [[('id', '=', 9)]],
    {'fields': ["user_id"]})
print(res)
#print(odoo.execute_kw('res.partner', 'search_read', [['id', '=', 1]], {'fields': ['user_id']}))
# print(env.execute_kw('res.partner', 'write', [[1], {
#     'name': "Newer partner"
# }]))
