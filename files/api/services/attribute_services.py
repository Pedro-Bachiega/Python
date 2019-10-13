from ...database.dao import AttributeDAO
from ...models.attribute import Attribute

def get_attributes_for_character(character_id: int) -> list:
    return AttributeDAO.get_attributes_for_character(character_id)

def get_attributes_for_world(world_id: int) -> list:
    return AttributeDAO.get_attributes_for_world(world_id)

def create_attribute(world_id: int, name: str, description: str, attr_type: str, negative_enabled: bool) -> int:    
    attribute = Attribute(-1, name, description, attr_type, negative_enabled)
    return AttributeDAO.create_attribute(world_id, attribute)