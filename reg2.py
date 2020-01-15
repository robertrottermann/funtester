import requests

# Fill in your details here to be posted to the login form.
base_url = "http://127.0.0.1:8069/registration_en"
rs_url = "http://127.0.0.1:8069/registration/student"
payload = {
    'login': 'student',
    'password': 'login'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(base_url, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print (p.text)

    # An authorised request.
    r = s.get(rs_url)
    print (r.text)