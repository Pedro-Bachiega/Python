from flask import json

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__, sort_keys = True)

    def __repr__(self):
        return self.toJson()

class CharacterResponse(JsonSerializable):
    def __init__(self, id, name, category, dead, active):
        self.id = id
        self.name = name
        self.category = category
        self.dead = dead
        self.active = active