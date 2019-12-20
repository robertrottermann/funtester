import requests

base_url = "http://localhost:8069/registration_en"
params = {
'HTTP_MAIL' : 'student',
'HTTP_SWISSEDUID' : '77',
'HTTP_GIVENNAME' : 'Student',
'HTTP_SURNAME' : 'Fleissig',
'HTTP_HOST' : 'localhost',
'HTTP_GENDER' : 'male',
'HTTP_DATEOFBIRTH' : '10.05.99',
'HTTP_TELEPHONENUMBER' : '031 333 10 20',
'HTTP_HOMEPOSTALADDRESS' : 'Sickingerstr 3, 3014, Bern',
'HTTP_HOMEPHONE' : '031 333 36 03',
'HTTP_MOBILE' : '079 222 42 07',
}
headers = {'Content-Type': 'application/text/html;'}
r = requests.get(base_url, params=params, headers=headers)
#r = requests.post(base_url,  headers=headers)
print(r.url)
print(r.status_code)

