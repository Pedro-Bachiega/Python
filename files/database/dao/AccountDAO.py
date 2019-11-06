from ...models.account import Account
from ..db_utils import Value
from .. import database_connector as db_conn

account_table_name = 'account'
banned_accounts_table_name = 'banned_accounts'

def get_account_for_id(account_id: int) -> Account:
    fields = ['account_id']
    values = [Value(account_id)]
    
    _, _, _, name = db_conn.select_one(account_table_name, fields, values)   
    return Account(account_id, '********', '********', name)

def get_account_for_login(user: str, password: str) -> Account:
    fields = ['user', 'password']
    values = [Value(user), Value(password)]
    account = None
    
    try:
        id, _, _, name = db_conn.select_one(account_table_name, fields, values)
        account = Account(id, '********', '********', name)
    except TypeError as e:
        print(e)
        pass
    
    return account

def create_account(account: Account) -> int:
    column_list = ['user', 'password', 'name']
    values = [Value(account.user), Value(account.password), Value(account.name)]
    return db_conn.insert(account_table_name, column_list, values)
    
def delete_account(account_id: int) -> int:
    fields = ['account_id']
    values = [Value(account_id)]
    return db_conn.delete(account_table_name, fields, values)

def ban_account(world_id: int, account_id: int) -> int:
    fields = ['world_id', 'account_id']
    values = [Value(world_id), Value(account_id)]
    return db_conn.insert(banned_accounts_table_name, fields, values)
