from . import JsonSerializable
        
class Stage(JsonSerializable):
    def __init__(self, stage_id: int, quest_id: int, stage_number: int, stage_question: str, decisions: list):
        self.stage_id = stage_id
        self.quest_id = quest_id
        self.stage_number = stage_number
        self.stage_question = stage_question
        self.decisions = decisions