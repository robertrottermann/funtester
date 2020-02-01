#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint
import os

class ModuleDataWriter(object):
    
    def __init__(self):        
        from sample_data.module_data import sample_data as s_data
        fname = os.path.abspath('%s/sample_data/data/module_data.py' % os.path.split(__file__)[0])
        keys = [
            "name",
            "short_name",
            "module_code",
            "module_id",
            "module_number",
            "semester_id",
            "ect_credist",
            "group",
            "guest",
            "kohorte_ids",
            "moodle_id",
            "number_of_events_to_visit",
            "repetition",
            "semester",
            "study_course_ids",
            "study_section_id",
            "type_of_exam",
            "type",
            "validation_state",
        ]
        
        vals_list = s_data.get('module_data').get('vals_list')
        result = []
        f = open(fname, 'w')
        f.write('data_list=[\n')
        for e_dic in vals_list:
            new_dic = {} #OrderedDict()
            for k in keys:
                new_dic[k] = e_dic[k]
            f.write('%s,\n' % pprint.pformat(new_dic))
        f.write('\n]\n')
        f.close()

ModuleDataWriter()