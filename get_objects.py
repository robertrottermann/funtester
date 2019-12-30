from xmlrpc import client
import json
import random
import requests

server_url = 'http://localhost:8069'
db_name = 'fernuni13'
username = 'admin'
password = 'admin'

# common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
# user_id = common.authenticate(db_name, username, password, {})

# models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)

# print(user_id, models)

json_endpoint = "%s/jsonrpc" % server_url
headers = {"Content-Type" : "application/json"}

def get_json_payload(service, method, *args):
    return  json.dumps({
        "jsonrpc": "2.0",
        "method" : "call",
        "params" : {
            "service" : service,
            "method" : method,
            "args" : args,
        },
        "id" : random.randint(0, 10000000)
    })

payload = get_json_payload("common", "login", db_name, username, password)
response = requests.post(json_endpoint, data=payload, headers=headers)
user_id = response.json()['result']

print(user_id)
search_domain = ['login', '=', 'admin']
payload = get_json_payload(
        "object",
        "execute_kw",
        db_name,
        user_id,
        password,
        'res.users',
        'search_read',
        [search_domain, ['id']]
    )
res = requests.post(json_endpoint, data=payload, headers=headers).json()
print(res)