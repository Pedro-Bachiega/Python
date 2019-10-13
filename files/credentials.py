import os
from xml.dom import minidom

configXml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.xml'))
configXml = minidom.parse(configXml_path)

xmlItems = configXml.getElementsByTagName('item')

database_ip = ''
database_name = ''
database_user = ''
database_password = ''
server_ip = ''
server_port = 0

for item in xmlItems:
    if item.attributes['name'].value == 'database_ip':
        database_ip = str(item.firstChild.data)
    elif item.attributes['name'].value == 'database_name':
        database_name = str(item.firstChild.data)
    elif item.attributes['name'].value == 'database_user':
        database_user = str(item.firstChild.data)
    elif item.attributes['name'].value == 'database_password':
        database_password = str(item.firstChild.data)
    elif item.attributes['name'].value == 'server_ip':
        server_ip = str(item.firstChild.data)
    elif item.attributes['name'].value == 'server_port':
        server_port = int(item.firstChild.data)

if database_ip == '':
    raise ValueError('No db ip provided')
elif database_name == '':
    raise ValueError('No db name provided')
elif database_user == '':
    raise ValueError('No db user provided')
elif database_password == '':
    raise ValueError('No db password provided')
elif server_ip == '':
    raise ValueError('No url provided')
elif server_port == 0:
    raise ValueError('No port provided')