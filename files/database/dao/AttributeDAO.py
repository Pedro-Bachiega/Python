from ...models.account import Account
from ...models.attribute import Attribute
from ..db_utils import Value
from .. import database_connector as db_conn

table_name = 'attribute'

def get_attributes_for_character(character_id: int) -> list:
    fields = ['character_id']
    values = [Value(character_id)]
    attribute_list = []
    
    try:
        db_list = db_conn.select(table_name, fields, values)
        
        if len(db_list) > 0:
            for i in range(0, len(db_list)):
                attr_id, world_id, name, description, attr_type, negative_enabled, default_value = db_list[i]
                attribute_list.append(Attribute(attr_id, name, description, attr_type, negative_enabled))
    except TypeError as e:
        print(e)
        pass
    
    return attribute_list

def get_attributes_for_world(world_id: int) -> list:
    fields = ['world_id']
    values = [Value(world_id)]
    attribute_list = []
    
    try:
        db_list = db_conn.select(table_name, fields, values)
        
        if len(db_list) > 0:
            for i in range(0, len(db_list)):
                attr_id, world_id, name, description, attr_type, negative_enabled, default_value = db_list[i]
                attribute_list.append(Attribute(attr_id, name, description, attr_type, negative_enabled, default_value))
    except TypeError as e:
        print(e)
        pass
    
    return attribute_list

def create_attribute(world_id: int, attribute: Attribute) -> int:
    negative_enabled = 1
    if attribute.negative_enabled:
        negative_enabled = 0
    
    fields = ['world_id', 'name', 'description', 'type', 'negative_enabled', 'default_value']
    values = [
        Value(world_id),
        Value(attribute.name),
        Value(attribute.description),
        Value(attribute.attr_type),
        Value(negative_enabled),
        Value(attribute.value)
    ]
    return db_conn.insert(table_name, fields, values)
