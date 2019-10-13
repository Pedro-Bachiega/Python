from ...database.dao import AccountDAO
from ...models.account import Account

def sign_up(user: str, password: str, name: str) -> int:
    return AccountDAO.create_account(user, password, name)

def sign_in(user: str, password: str) -> Account:
    return AccountDAO.get_account_for_login(user, password)

def get_account_for_id(account_id: int) -> Account:
    return AccountDAO.get_account_for_id(account_id)

def delete_account(account_id: int) -> int:
    return AccountDAO.delete_account(account_id)

def ban_account(world_id: int, account_id: int) -> int:
    return AccountDAO.ban_account(world_id, account_id)
