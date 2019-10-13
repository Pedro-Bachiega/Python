from flask import json

class JsonSerializable(object):
    def to_json(self):
        json_result = json.dumps(self.__dict__, sort_keys = True)
        print(json_result)
        return json_result

    def __repr__(self):
        return self.to_json()