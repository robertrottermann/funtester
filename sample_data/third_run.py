#!/usr/bin/env python
# -*- coding: utf-8 -*-
from odoo_handler import get_objects
from . event_presence import sample_data as event_presence_data

sample_data = {}
for s_data in [
        event_presence_data,
    ]:
    sample_data.update(s_data)
