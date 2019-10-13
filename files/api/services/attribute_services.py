from ...database.dao import AttributeDAO
from ...models.attribute import Attribute
from ...utils import convert_list_to_json_list

def get_attributes_for_character(character_id: int) -> list:
    attrs = AttributeDAO.get_attributes_for_character(character_id)
    return convert_list_to_json_list(attrs)

def get_attributes_for_world(world_id: int) -> list:
    attrs = AttributeDAO.get_attributes_for_world(world_id)
    return convert_list_to_json_list(attrs)

def create_attribute(world_id: int, name: str, description: str, attr_type: str, negative_enabled: bool) -> int:    
    return AttributeDAO.create_attribute(world_id, Attribute(-1, name, description, attr_type, negative_enabled))