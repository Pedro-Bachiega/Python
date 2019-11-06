from ...database.dao import QuestDAO
from ...models.quest import Quest, QuestReward, Stage, Decision
from ...utils import convert_list_to_json_list

def create_quest(json: str) -> int:
    return QuestDAO.create_quest(Quest(json))