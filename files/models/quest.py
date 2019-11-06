from .json_serializable import JsonSerializable
        
class Quest(JsonSerializable):
    def create_stages_from_json(self, json: str) -> list:
        stage_list = []
        
        for stage in json['stages']:
            stage_list.append(Stage(stage))
        return stage_list
        
    def create_rewards_from_json(self, json: str) -> list:
        reward_list = []
        
        for reward in json['rewards']:
            reward_list.append(QuestReward(reward))
        return reward_list
    
    def __init__(self, json: str):
        self.quest_id = -1
        self.name = json['name']
        self.description = json['description']
        self.suggested_level = json['suggested_level']
        self.stages = create_stages_from_json(json)
        self.rewards = create_rewards_from_json(json)
    
    def __init__(self, quest_id: int, world_id: int, name: str, description: str, suggested_level: int, stages: list, rewards: list):
        self.quest_id = quest_id
        self.name = name
        self.description = description
        self.suggested_level = suggested_level
        self.stages = stages
        self.rewards = rewards
        
class Stage(JsonSerializable):
    def create_decisions_from_json(self, json: str) -> list:
        decision_list = []
        
        for decision in json['decisions']:
            decision_list.append(Decision(decision))
        return decision_list
    
    def __init__(self, json: str):
        self.stage_id = json['stage_id']
        self.stage_number = json['stage_number']
        self.stage_question = json['stage_question']
        self.decisions = create_decisions_from_json(json)
        
    def __init__(self, stage_id: int, stage_number: int, stage_question: str, decisions: list):
        self.stage_id = stage_id
        self.stage_number = stage_number
        self.stage_question = stage_question
        self.decisions = decisions
        
class QuestReward(JsonSerializable):
    def __init__(self, json: str):
        self.attribute_id = json['attribute_id']
        self.value = json['value']
    
    def __init__(self, attribute_id: int, value: str):
        self.attribute_id = attribute_id
        self.value = value
        
class Decision(JsonSerializable):
    def __init__(self, json: str):
        self.decision_id = json['decision_id']
        self.label = json['label']
        self.success_chance = json['success_chance']
        self.success_message = json['success_message']
        self.failure_message = json['failure_message']
        
    def __init__(self, decision_id: int, stage_id: int, label: str, success_chance: int, success_message: str, failure_message: str):
        self.decision_id = decision_id
        self.label = label
        self.success_chance = success_chance
        self.success_message = success_message
        self.failure_message = failure_message