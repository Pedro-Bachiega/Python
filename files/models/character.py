from . import JsonSerializable
        
class Character(JsonSerializable):
    def __init__(self, character_id: int, account_id: int, world_id: int, name: str, level: int):
        self.character_id = character_id
        self.account_id = account_id
        self.world_id = world_id
        self.name = name
        self.level = level
        self.attributes = []
        
    def __init__(self, character_id: int, account_id: int, world_id: int, name: str, level: int, attributes: list):
        self.character_id = character_id
        self.account_id = account_id
        self.world_id = world_id
        self.name = name
        self.level = level
        self.attributes = attributes