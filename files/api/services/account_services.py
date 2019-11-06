from ...database.dao import AccountDAO
from ...models.account import Account

def sign_up(json: str) -> int:
    return AccountDAO.create_account(Account(json))

def sign_in(json: str) -> Account:
    account = AccountDAO.get_account_for_login(json['user'], json['password'])
    return account.__repr__()

def get_account_for_id(account_id: int) -> Account:
    account = AccountDAO.get_account_for_id(account_id)
    return account.__repr__()

def delete_account(account_id: int) -> int:
    return AccountDAO.delete_account(account_id)

def ban_account(world_id: int, account_id: int) -> int:
    return AccountDAO.ban_account(world_id, account_id)
