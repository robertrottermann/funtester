#!/usr/bin/env python
# # -*- coding: utf-8 -*-
import os
from argparse import Namespace

BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
DATA_POOL = {}  # values to be set in the second run


def get_config_from_yaml(which=["config"], result_dic={}):
    """[read config data from yaml files]
    return dict with config data dicts
    """
    # the base info we need to access the various parts of erp-workbench
    # it is in the config.yaml file in the erp-workbench config folder
    from construct_defaults import check_and_update_base_defaults

    construct_result = {}
    yaml_dic = {}
    for y_info in (("config", "base_info.py"),):
        y_name, file_name = y_info
        if y_name not in which:
            continue
        config_yaml = "%s/%s.yaml" % (BASE_PATH, y_name)
        if not os.path.exists(config_yaml):
            # in_file = "%s.in" % config_yaml
            from shutil import copyfile

            copyfile("%s/%s.yaml.in" % (BASE_PATH, y_name), config_yaml)
        # build a list to be sent to check_and_update_base_defaults
        yaml_dic[y_name] = (
            y_name,
            config_yaml,
            "%s/config/%s" % (BASE_PATH, file_name),
            "%s/%s.yaml.in" % (BASE_PATH, y_name),
        )
        vals = {
            #'USER_HOME' : user_home,
            #'BASE_PATH' : BASE_PATH,
            #'ACT_USER'  : ACT_USER,
            #'DB_USER'   : ACT_USER,
            #'PROJECT_INSTALL': '%(inner_path)s',
            #'SITE_DATA_DIR' : '%(site_data_dir)s',
            #'ERP_VERSION' : '%(erp_version)s',
        }
        # must_reload flags whether we need do restart
        must_reload = check_and_update_base_defaults(
            yaml_dic.values(), vals, construct_result
        )
        # update the result dic, so the caller can access it
        result_dic.update(yaml_dic)
        # return dictionary with the values
        return must_reload


# def construct_loader_values(val_name, method, params):
# """construct an empty class as placeholder value that is replace by real data in the second run

# Arguments:
# val_name {string} -- name of the value, will be made unique
# method {string} --  method to collect data like 'get_objects("study.course")'

# Returns:
# [object] -- placeholder that will be replaced
# """

# class DATA_POOL_OBJECT(object):
# """dummy class to create object with to hold deferred values
# """

# pass

# retval = DATA_POOL_OBJECT()
# has_val_name = DATA_POOL.get(val_name)
# val_name_ori = val_name
# counter = 0
# while has_val_name:
# counter += 1
# val_name = "%s%s" % (val_name_ori, counter)
# has_val_name.get(val_name)
## construct a global name
# globals()[val_name] = retval
## collect all placeholders in a pool, so we can replace them before the second run
# DATA_POOL[val_name] = {'retval' : retval, 'method' : method, 'params' : params}
# return retval


class MyNamespace(Namespace):
    # we need a namespace that just ignores unknow options
    def __getattr__(self, key):
        if key in self.__dict__.keys():
            return self.__dict__[key]
        return None
