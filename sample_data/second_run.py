#!/usr/bin/env python
# -*- coding: utf-8 -*-
from odoo_handler import get_objects
from . module_data import sample_data as module_data_data
from . kohorte import sample_data as kohorte_data
from . studies import sample_data as studies_data
from . credit import sample_data as credit_data
from . people import sample_data as people_data
from . student_semester import sample_data as ss_data
from . student_module import sample_data as sm_data

sample_data = {}
for s_data in [
        module_data_data,
        kohorte_data,
        studies_data,
        credit_data,
        people_data,
        ss_data,
        sm_data
    ]:
    sample_data.update(s_data)
