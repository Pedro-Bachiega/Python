from . import JsonSerializable
        
class QuestReward(JsonSerializable):
    def __init__(self, attribute_id: int, value: str):
        self.attribute_id = attribute_id
        self.value = value