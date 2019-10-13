from flask import json

class JsonSerializable(object):
    def to_json(self):
        return json.dumps(self.__dict__, sort_keys = True)

    def __repr__(self):
        return self.to_json()