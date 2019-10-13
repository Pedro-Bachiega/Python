from ...database.dao import AttributeDAO, CharacterDAO
from ...database.db_utils import DUPLICATE_ENTRY
from ...models.character import Character
from ...utils import convert_list_to_json_list

def create_character(account_id:int, world_id: int, name: str) -> int:
    attributes = AttributeDAO.get_attributes_for_world(world_id)
    result = CharacterDAO.create_character(Character(-1, account_id, world_id, name, 1, []))
    
    if result != DUPLICATE_ENTRY and len(attributes) > 0:
        attr_result = AttributeDAO.insert_attributes_for_character(character_id = result, attributes = attributes)
        
    return result

def get_characters_for_account(account_id: int, world_id: int) -> list:
    characters = CharacterDAO.get_characters_for_account(account_id, world_id)
    
    if len(characters) > 0:
        for i in range(len(characters)):
            attrs = AttributeDAO.get_attributes_for_character(characters[i].character_id)
            characters[i].attributes = convert_list_to_json_list(attrs)
    
    return convert_list_to_json_list(characters)

def get_character_details(character_id: int) -> Character:
    char = CharacterDAO.get_character(character_id)
    attrs = AttributeDAO.get_attributes_for_character(character_id)
    char.attributes = attrs
    return char.__repr__()
