#!/usr/bin/env python
# -*- coding: utf-8 -*-
from odoo_handler import get_objects
from . location import sample_data as location_data
from . room import sample_data as room_data
from . study_course import sample_data as study_course_data
from . study_section import sample_data as study_section_data
from . student import sample_data as student_data
from . function import sample_data as function_data
from . modules import sample_data as module_data
from . semester import sample_data as semester_data
from . price_event import sample_data as price_event_data
from . university import sample_data as university_data
from . study_center import sample_data as study_center_data
from . department import sample_data as department_data
from . grade import sample_data as grade_data
from . reason_exmatriculation import sample_data as reason_exmatriculation_data
from . studies import sample_data as studies_data
from . account_analytic_account import sample_data as account_analytic_account_data



sample_data = {}
for s_data in [
        location_data,
        room_data,
        study_course_data,
        study_section_data,
        student_data,
        function_data,
        module_data,
        semester_data,
        price_event_data,
        university_data,
        study_center_data,
        department_data,
        grade_data,
        reason_exmatriculation_data,
        studies_data,
        account_analytic_account_data,

    ]:
    sample_data.update(s_data)
