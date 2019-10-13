def convert_list_to_json_list(regular_list: list):
    if len(regular_list) > 0:
        json_list = []
        
        for i in range(len(regular_list)):
            json_list.append(regular_list[i].__repr__())
            
        return json_list
    else:
        return regular_list