#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bcolors import bcolors

# -------------------------------------
# messages
# -------------------------------------
HOPPALA_AN_ERROR = """%s------------------------------------------------
HOPPALLA an error happend:
%%s
------------------------------------------------%s
""" % (
    bcolors.FAIL,
    bcolors.ENDC,
)
ERP_NOT_RUNNING = """%s------------------------------------------------
Site %%s seems not to run!
------------------------------------------------%s
""" % (
    bcolors.FAIL,
    bcolors.ENDC,
)
ERP_NOT_RUNNING_PW = """%s------------------------------------------------
Site %%s seems not to run!
Or it was not possible to login as
user: %%s
using pw: %%s
------------------------------------------------%s
""" % (
    bcolors.FAIL,
    bcolors.ENDC,
)
COULD_NOT_FIND_OBJECT = """%s------------------------------------------------
The search for an object in
model: %%s
with search condition: %%s
did not yield in a result.
Please check sample_data.py
------------------------------------------------%s
""" % (
    bcolors.FAIL,
    bcolors.ENDC,
)
VALUES_CHANGED = """%s------------------------------------------------
The config values have changed please check the files in %%s/config/
If wrong please adapt %%s/config.yaml
------------------------------------------------%s
""" % (
    bcolors.WARNING,
    bcolors.ENDC,
)
MODULE_NOT_FOUND = """%s------------------------------------------------
File %%s
for module %%s
not found
------------------------------------------------%s
""" % (
    bcolors.FAIL,
    bcolors.ENDC,
)
MODULE_DATA_CHANGED = """%s------------------------------------------------
Some odoo modules have been patched with data from
patches.py
Please restart odoo!
and reinstall %%s
This can be done by rerunning install_test -s fernuni
------------------------------------------------%s
""" % (
    bcolors.WARNING,
    bcolors.ENDC,
)
