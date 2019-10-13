from files.database.dao import AccountDAO, WorldDAO
from files.api.services import account_services
from files.api.routes import app
from files.credentials import server_ip, server_port

app.run(host=server_ip, port=server_port, debug=True)