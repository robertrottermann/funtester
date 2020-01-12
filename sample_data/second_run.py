#!/usr/bin/env python
# -*- coding: utf-8 -*-
from odoo_handler import get_objects
from . module_data import sample_data as module_data_data
from . kohorte import sample_data as kohorte_data

sample_data = {}
for s_data in [
        module_data_data,
        kohorte_data
    ]:
    sample_data.update(s_data)
