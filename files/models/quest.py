from .json_serializable import JsonSerializable
        
class Quest(JsonSerializable):
    def __init__(self, quest_id: int, world_id: int, name: str, description: str, suggested_level: int, finished: bool, stages: list, rewards: list):
        self.quest_id = quest_id
        self.world_id = world_id
        self.name = name
        self.description = description
        self.suggested_level = suggested_level
        self.finished = finished
        self.stages = stages
        self.rewards = rewards