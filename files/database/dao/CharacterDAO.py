from ...models.attribute import Attribute
from ...models.character import Character
from ..db_utils import Value, DUPLICATE_ENTRY
from .. import database_connector as db_conn

character_table_name = 'character'

def create_character(character: Character) -> int:
    fields = ['world_id', 'account_id', 'name', 'level']
    values = [Value(character.world_id), Value(character.account_id), Value(character.name), Value(character.level)]
    return db_conn.insert(character_table_name, fields, values)
    
def get_characters_for_account(account_id: int, world_id: int) -> list:
    char_list = []
    fields = ['world_id', 'account_id']
    values = [Value(world_id), Value(account_id)]
    db_list = db_conn.select(character_table_name, fields, values)
    
    if len(db_list) > 0:
        for i in range(0, len(db_list)):
            char_id, _, _, name, level = db_list[i]
            char_list.append(Character(char_id, account_id, world_id, name, level, []))
            
    return char_list

def get_character(character_id: int) -> Character:
    fields = ['character_id']
    values = [Value(character_id)]
    
    _, char_world_id, char_account_id, name, level = db_conn.select_one(character_table_name, fields, values)
    return Character(character_id, char_world_id, char_account_id, name, level, [])
    