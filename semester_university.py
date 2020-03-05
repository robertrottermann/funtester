2020-03-03 06:04:17,145 13259 DEBUG fernuni13 odoo.api: call semester.university(1,).read(['active', 'university_id', 'semester_id', 'academic_start', 'acedemic_end', 'semester_reinscription', 'lecture_period_start', 'lecture_period_end', 'exam_session_start', 'exam_session_end', 'exam_inscription', 'registration_regular_end', 'registration_extended_end', 'datum_diplomfeier', 'remarks', 'display_name'])
2020-03-03 06:04:17,154 13259 DEBUG fernuni13 odoo.http.rpc.response: call_kw: semester.university read: time:0.008s mem: 311216.0k -> 311216.0k (diff: 0.0k), [{'academic_start': datetime.date(2020, 1, 5),
  'acedemic_end': datetime.date(2020, 6, 5),
  'active': True,
  'datum_diplomfeier': datetime.date(2020, 6, 19),
  'display_name': 'Spring term 2020',
  'exam_inscription': datetime.date(2020, 3, 3),
  'exam_session_end': datetime.date(2020, 5, 2),
  'exam_session_start': datetime.date(2020, 4, 1),
  'id': 1,
  'lecture_period_end': datetime.date(2020, 3, 12),
  'lecture_period_start': datetime.date(2020, 1, 15),
  'registration_extended_end': datetime.date(2020, 3, 19),
  'registration_regular_end': datetime.date(2020, 3, 18),
  'remarks': 'No remarks',
  'semester_id': (27, 'Spring term 2020'),
  'semester_reinscription': datetime.date(2020, 4, 15),
  'university_id': False}]
2020-03-03 06:04:17,155 13259 INFO fernuni13 werkzeug: 127.0.0.1 - - [03/Mar/2020 06:04:17] "POST /web/dataset/call_kw/semester.university/read HTTP/1.1" 200 - 5 0.003 0.015
2020-03-03 06:04:38,198 13259 DEBUG fernuni13 odoo.http.rpc.response: poll: None None: time:50.017s mem: 311216.0k -> 311216.0k (diff: 0.0k), []
2020-03-03 06:04:38,200 13259 INFO fernuni13 werkzeug: 127.0.0.1 - - [03/Mar/2020 06:04:38] "POST /longpolling/poll HTTP/1.1" 200 - 8 0.003 50.020
2020-03-03 06:04:38,209 13259 DEBUG fernuni13 odoo.modules.registry: Multiprocess signaling check: [Registry - 24 -> 24] [Cache - 923 -> 923]
2020-03-03 06:04:38,214 13259 DEBUG fernuni13 odoo.http.rpc.request: poll: None None, []
2020-03-03 06:05:28,229 13259 DEBUG fernuni13 odoo.http.rpc.response: poll: None None: time:50.015s mem: 311216.0k -> 311216.0k (diff: 0.0k), []
2020-03-03 06:05:28,230 13259 INFO fernuni13 werkzeug: 127.0.0.1 - - [03/Mar/2020 06:05:28] "POST /longpolling/poll HTTP/1.1" 200 - 8 0.003 50.020
2020-03-03 06:05:28,239 13259 DEBUG fernuni13 odoo.modules.registry: Multiprocess signaling check: [Registry - 24 -> 24] [Cache - 923 -> 923]
2020-03-03 06:05:28,244 13259 DEBUG fernuni13 odoo.http.rpc.request: poll: None None, []



2020-03-03 06:10:29,836 13259 DEBUG fernuni13 odoo.api: call semester.university(1,).read(['active', 'university_id', 'semester_id', 'academic_start', 'acedemic_end', 'semester_reinscription', 'lecture_period_start', 'lecture_period_end', 'exam_session_start', 'exam_session_end', 'exam_inscription', 'registration_regular_end', 'registration_extended_end', 'datum_diplomfeier', 'remarks', 'display_name'])
2020-03-03 06:10:29,844 13259 DEBUG fernuni13 odoo.http.rpc.response: call_kw: semester.university read: time:0.007s mem: 311216.0k -> 311216.0k (diff: 0.0k), [{'academic_start': datetime.date(2020, 1, 5),
  'acedemic_end': datetime.date(2020, 6, 5),
  'active': True,
  'datum_diplomfeier': datetime.date(2020, 6, 19),
  'display_name': 'Spring term 2020',
  'exam_inscription': datetime.date(2020, 3, 3),
  'exam_session_end': datetime.date(2020, 5, 2),
  'exam_session_start': datetime.date(2020, 4, 1),
  'id': 1,
  'lecture_period_end': datetime.date(2020, 3, 12),
  'lecture_period_start': datetime.date(2020, 1, 15),
  'registration_extended_end': datetime.date(2020, 3, 19),
  'registration_regular_end': datetime.date(2020, 3, 18),
  'remarks': 'No remarks\nZweite zeile',
  'semester_id': (27, 'Spring term 2020'),
  'semester_reinscription': datetime.date(2020, 4, 15),
  'university_id': False}]
2020-03-03 06:10:29,845 13259 INFO fernuni13 werkzeug: 127.0.0.1 - - [03/Mar/2020 06:10:29] "POST /web/dataset/call_kw/semester.university/read HTTP/1.1" 200 - 3 0.001 0.012
2020-03-03 06:11:18,454 13259 DEBUG fernuni13 odoo.http.rpc.response: poll: None None: time:50.018s mem: 311216.0k -> 311216.0k (diff: 0.0k), []
2020-03-03 06:11:18,455 13259 INFO fernuni13 werkzeug: 127.0.0.1 - - [03/Mar/2020 06:11:18] "POST /longpolling/poll HTTP/1.1" 200 - 8 0.003 50.023
2020-03-03 06:11:18,464 13259 DEBUG fernuni13 odoo.modules.registry: Multiprocess signaling check: [Registry - 24 -> 24] [Cache - 923 -> 923]
2020-03-03 06:11:18,467 13259 DEBUG fernuni13 odoo.http.rpc.request: poll: None None, []
