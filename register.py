# https://realpython.com/python-requests/
import requests

"""
in the registration form only departments are shown with the 
 [('visibility_registration', '=', True)]
 set
"""

base_url = "http://127.0.0.1:8069/registration_en"
base_url = "http://localhost:8069/registration_en"
base_url = "http://127.0.0.1:8069/registration/student"

headers = {
    "MAIL": "robert@redcor.ch",
    "SWISSEDUID": "77378",
    "GIVENNAME": "Student4",
    "SURNAME": "Fleissig4",
#    "HOST": "fernuni.ch",
    "HOST": "unidistance.ch",
    "GENDER": "male",
    "DATEOFBIRTH": "10-05-1999",
    "TELEPHONENUMBER": "031 333 10 20",
    "HOMEPOSTALADDRESS": "Sickingerstr 3$3014$3013 Bern$Switzerland",
    "HOMEPHONE": "031 333 36 04",
    "MOBILE": "079 222 42 07",
    "Content-Type": "application/text/html;",
}
params = {}
# headers = {'Content-Type': 'application/text/html;'}
r = requests.get(base_url, params=params, headers=headers)
# r = requests.post(base_url,  headers=headers)
print(r.url)
print(r.status_code)


# request.session.authenticate(
#     request.session.db, user.login,
#     '$pbkdf2-sha512$25000$8H4vBQCgFILQOgdgLIUQwg$YjdrAi/MMddKpv4NAfr7Jd2MwiBJi.11wZcumuvNJMy0Pf4R3TjB0fUWCa.o9ow8SGUQYdvXyiNDoyozw1JRBA'
# )
