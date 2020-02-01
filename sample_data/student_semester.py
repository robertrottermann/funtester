#!/usr/bin/env python
# # -*- coding: utf-8 -*-
from odoo_handler import get_objects
"""
make sure, that study for partner is NOT in exmatriculated state
update studies set state_of_study = 'student'  where partner_id=(select id from res_partner where name='Jürgen');
"""
RD_DISP="""
1) Wenn immer es die Situation erlaubt, sind die Präsenzveranstaltungen ordentlich zu besuchen.
2) Die übrigen geforderten Leistungen (insb. die Bearbeitung der Einsendeaufgaben) sind ordentlich und fristgemäss zu erbringen.
3) Für jede Präsenzveranstaltung, die nicht besucht wird, ist der zu behandelnde Stoff eigenständig in einem schriftlichen Essay zusammenzufassen und dem/r entsprechenden Modulassistent/In bis spätestens 7 Tage nach dem Präsenztermin zuzustellen. Der hierzu benötigte zeitliche Aufwand hat der zeitlichen Beanspruchung der Präsenzveranstaltung mindestens gleichzukommen.
4) Der/die Gesuchssteller/in ist sich im Klaren darüber, dass die an den Präsenzveranstaltungen behandelten Themen prüfungsrelevant sind. Er/Sie ist selber dafür verantwortlich, dass er/sie via Kommilitonen Kenntnis über die dozierten Inhalte erhält und in Besitz allfällig verteilter Materialien gelangt.
"""
sample_data = {
    "student_semester" : {
        "step": "second_run",
        "module" : "student.semester",
        "search": ['studies_id', 'semester_id'],
        "vals_list": [
            {
                'choose_student_module_finished': True,
                'date_card_transmitted': '2019-12-30',
                'invoice_id': False,
                'iuv': 'I',
                'part_time': False,
                'remark_dispensation': False,
                'remarks_immatriculation': False,
                'semester_id': ("semester", [("short_name", "FS20")]),
                'state_student_semester': '1',
                'student_module_by_wizard': False,
#                'studies_id': ("studies", 'partner_id', ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")])
                "studies_id": ("studies", [("partner_id", ("res.partner", [("name", "Jürgen"), ("last_name", "Beer")]))]), #1, # SUCHEN!!
                'regular_student': True
            },
            {
                'choose_student_module_finished': True,
                'date_card_transmitted': '2019-12-30',
                'invoice_id': False,
                'invoice_paid': True,
                'iuv': 'I',
                'part_time': True,
                'remark_dispensation': RD_DISP,
                'remarks_immatriculation': False,
                'semester_id': ("semester", [("short_name", "FS16")]),
                'state_student_semester': '1',
                'student_module_by_wizard': False,
                "studies_id": ("studies", [("partner_id", ("res.partner", [("name", "Patrizia"), ("last_name", "Bardola")]))]), #1, # SUCHEN!!
                'regular_student': True
            },
        ]
    },
}
