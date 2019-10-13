from ...models.world import World
from ..db_utils import Value
from .. import database_connector as db_conn
from random import randint

world_table_name = 'world'

def create_world(account_id: int, name: str) -> int:
    fields = ['creator_account_id', 'public_id', 'name']
    values = [Value(account_id), Value(randint(1, 99999999999)), Value(name)]
    
    world_id = db_conn.insert(world_table_name, fields, values)
    response = None
    if world_id == -2:
        response = create_world(account_id, name)
    else:
        response = world_id
    print(response)
    return response

def get_worlds_for_account(creator_account_id: int) -> list:
    fields = ['creator_account_id']
    values = [Value(creator_account_id)]
    world_list = []
    response = None
    
    try:
        account_worlds = db_conn.select(world_table_name, fields, values)
        
        for i in range(0, len(account_worlds)):
            id, account_id, public_id, name = account_worlds[i]
            world_list.append(World(id, account_id, public_id, name))
        
        response = world_list
    except TypeError as e:
        response = {'error': 'NO WORLDS FOUND FOR account_id:%s'%creator_account_id}
        print(e)
        pass
    
    return response
    
def get_world_for_public_id(public_id: int) -> World:
    fields = ['public_id']
    values = [Value(public_id)]
    world = None
    
    try:
        id, account_id, public_id, name = db_conn.select_one(world_table_name, fields, values)
        world = World(id, account_id, public_id, name)
    except TypeError as e:
        print(e)
        pass
    
    return world
    
def delete_world(world_id: int) -> int:
    fields = ['world_id']
    values = [Value(world_id)]
    return db_conn.delete(world_table_name, fields, values)