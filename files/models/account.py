from .json_serializable import JsonSerializable

class Account(JsonSerializable):
    def __init__(self, account_id: int, user: str, password: str, name: str):
        self.account_id = account_id
        self.user = user
        self.password = password
        self.name = name