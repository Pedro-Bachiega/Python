from ...models.quest import Decision, Quest, QuestReward, Stage
from ..db_utils import Value
from .. import database_connector as db_conn

decision_table_name = 'decision'
quest_table_name = 'quest'
quest_reward_table_name = 'quest_reward'
stage_table_name = 'stage'

def create_quest(world_id: int, quest: Quest) -> int:
    fields = ['world_id', 'name', 'description', 'suggested_level']
    values = [Value(world_id), Value(quest.name), Value(quest.description), Value(quest.suggested_level)]
    quest_id = db_conn.insert(quest_table_name, fields, values)
    
    for i in range(0, len(quest.rewards)):
        create_quest_reward(quest_id, quest.rewards[i])
        
    for i in range(0, len(quest.stages)):
        create_stage(quest_id, quest.stages[i])
        
    return quest_id

def create_quest_reward(quest_id: int, quest_reward: QuestReward) -> int:
    fields = ['quest_id', 'attribute_id', 'value']
    values = [Value(quest_id), Value(quest_reward.attribute_id), Value(quest_reward.value)]
    return db_conn.insert(quest_reward_table_name, fields, values)

def create_stage(quest_id: int, stage: Stage):
    fields = ['quest_id', 'stage_number', 'stage_question']
    values = [Value(quest_id), Value(stage.stage_number), Value(stage.stage_question)]
    stage_id = db_conn.insert(stage_table_name, fields, values)
    
    for i in range(0, len(stage.decisions)):
        create_decision(stage_id, stage.decisions[i])
        
    return stage_id

def create_decision(stage_id: int, decision: Decision) -> int:
    fields = ['stage_id', 'label', 'success_chance', 'success_message', 'failure_message']
    values = [Value(stage_id), Value(decision.label), Value(decision.success_chance), Value(decision.success_message), Value(decision.failure_message)]
    return db_conn.insert(decision_table_name, fields, values)