from copy import deepcopy

#def create_diff(data1, data2):


    #for key in keys:
        ####return diff


def get_diff_key(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = []
    dict_ = {}

    for key in keys:
        data1_value = data1.get(key)
        data2_value = data2.get(key)

        if key in data1 and key not in data2:
            dict_['status'] = 'removed'
            dict_['old_value'] = data1_value

        elif key in data1 and key in data2:
            if data1_value == data2_value:
                dict_['status'] = 'unchanged'
                dict_["old_value"] = data1_value
        
        elif isinstance(data1_value, dict) and isinstance(data2_value, dict):
            dict_['status'] = 'nested'
            dict_['nested'] = data1_value, data2_value
        
        elif key not in data1 and key in data2:
            dict_['status'] = 'added'
            dict_['new_value'] = data2_value
        
        else:
            dict_['status'] = 'updated'
            dict_['old_value'] = data1_value
            dict_['new_value'] = data2_value

    return diff.append(deepcopy(dict_))
