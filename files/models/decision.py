from . import JsonSerializable
        
class Decision(JsonSerializable):
    def __init__(self, decision_id: int, stage_id: int, label: str, success_chance: int, success_message: str, failure_message: str):
        self.decision_id = decision_id
        self.stage_id = stage_id
        self.label = label
        self.success_chance = success_chance
        self.success_message = success_message
        self.failure_message = failure_message