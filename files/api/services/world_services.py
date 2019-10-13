from ...database.dao import WorldDAO
from ...utils import convert_list_to_json_list

def create_world(account_id: int, name: str):
    return WorldDAO.create_world(account_id, name)

def get_account_worlds(account_id: int):
    worlds = WorldDAO.get_worlds_for_account(account_id)
    return convert_list_to_json_list(worlds)

def get_world_for_public_id(public_id: int):
    world = WorldDAO.get_world_for_public_id(public_id)
    return world.__repr__()

def delete_world(world_id: int):
    return WorldDAO.delete_world(world_id)
