from ...database.dao import AttributeDAO
from ...models.attribute import Attribute
from ...utils import convert_list_to_json_list

def get_attributes_for_character(character_id: int) -> list:
    attrs = AttributeDAO.get_attributes_for_character(character_id)
    return convert_list_to_json_list(attrs)

def get_attributes_for_world(world_id: int) -> list:
    attrs = AttributeDAO.get_attributes_for_world(world_id)
    return convert_list_to_json_list(attrs)

def create_attribute(json: str) -> int:
    return AttributeDAO.create_attribute(json['world_id'], Attribute(json))

def insert_attributes_for_character(character_id: int, attributes: list):
    return AttributeDAO.insert_attributes_for_character(character_id, attributes)