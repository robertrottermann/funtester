from xmlrpc import client

server_url = 'http://localhost:8069'
db_name = 'fernuni13'
username = 'admin'
password = 'admin'

common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)

print(user_id, models)