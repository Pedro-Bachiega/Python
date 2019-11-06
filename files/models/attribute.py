from .json_serializable import JsonSerializable

class Attribute(JsonSerializable):
    def get_default_value(self, attr_type: str):
        if attr_type == 'text':
            return ''
        else:
            return '0'
        
    def __init__(self, json: str):
        self.id = -1
        self.name = json['name']
        self.description = json['description']
        self.attr_type = json['attr_type']
        self.negative_enabled = json['negative_enabled'] == 'true'
        self.value = self.get_default_value(attr_type)
        
    def __init__(self, id: int, name: str, description: str, attr_type: str, negative_enabled: bool, value: str):
        self.id = id
        self.name = name
        self.description = description
        self.attr_type = attr_type
        self.negative_enabled = negative_enabled
        self.value = value