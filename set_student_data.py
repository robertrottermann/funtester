#!/usr/bin/env python
# -*- coding: utf-8 -*-
funid_registration/controller/main.py: ~1860
        studies = studies_obj.sudo().search([
            ('partner_id', '=', registration.user_id.partner_id.id),
            ('study_course_id', '=', registration.study_course_id.id),
            ('state_of_study', 'in',
             ['registered_1', 'registered_2', 'student',
              'temporally_allowed', 'definitely_allowed'])
        ])
