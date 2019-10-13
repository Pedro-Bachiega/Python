#Generic model
def find_value_type(value) -> str:
    result = ''
    value_type = '%s'%type(value)
    
    if 'str' in value_type:
        result = 'text'
    else:
        result = 'number'
        
    return result
    
class Value(object):
    def __init__(self, value):
        self.value = value
        self.type = find_value_type(value)

#Errors
DUPLICATE_ENTRY = -2