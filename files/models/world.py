from .json_serializable import JsonSerializable
        
class World(JsonSerializable):
    def __init__(self, world_id: int, creator_account_id: int, public_id: int, name: str):
        self.world_id = world_id
        self.creator_account_id = creator_account_id
        self.public_id = public_id
        self.name = name