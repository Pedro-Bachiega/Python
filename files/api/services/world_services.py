from ...database.dao import WorldDAO

def create_world(account_id: int, name: str):
    return WorldDAO.create_world(account_id, name)

def get_account_worlds(account_id: int):
    return WorldDAO.get_worlds_for_account(account_id)

def get_world_for_public_id(public_id: int):
    return WorldDAO.get_world_for_public_id(public_id)

def delete_world(world_id: int):
    return WorldDAO.delete_world(world_id)
