from ...models.account import Account
from ...models.attribute import Attribute
from ..db_utils import Value
from .. import database_connector as db_conn

attributes_table_name = 'attribute'
character_attributes_table_name = 'character_attributes'

def get_attributes_for_character(character_id: int) -> list:
    attribute_list = []
    command_portions = []
    command_portions.append('SELECT attribute.attribute_id, attribute.world_id, attribute.name, attribute.description, attribute.type, attribute.negative_enabled, character_attributes.value')
    command_portions.append('FROM character_attributes')
    command_portions.append('INNER JOIN attribute ON character_attributes.attribute_id = attribute.attribute_id')
    command_portions.append('WHERE character_attributes.character_id = %s'%character_id)
    command = ' '.join(command_portions)
    
    try:
        db_list = db_conn.custom_select(command, False)
        
        if len(db_list) > 0:
            for i in range(0, len(db_list)):
                attr_id, world_id, name, description, attr_type, negative_enabled, value = db_list[i]
                attribute_list.append(Attribute(attr_id, name, description, attr_type, negative_enabled, value))
    except TypeError as e:
        print(e)
        pass
    
    return attribute_list
    
def insert_attributes_for_character(character_id: int, attributes: list):
    fields = ['character_id', 'attribute_id', 'value']
    
    if len(attributes) > 0:
        for i in range(len(attributes)):
            attribute = attributes[i]
            values = [Value(character_id), Value(attribute.id), Value(attribute.value)]
            db_conn.insert(character_attributes_table_name, fields, values)

def get_attributes_for_world(world_id: int) -> list:
    fields = ['world_id']
    values = [Value(world_id)]
    attribute_list = []
    
    try:
        db_list = db_conn.select(attributes_table_name, fields, values)
        
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
    return db_conn.insert(attributes_table_name, fields, values)
