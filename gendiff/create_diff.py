def get_diff_key(data1, data2, key='key'):
    """Получает разницу между двумя словарями"""

    keys = sorted(data1.keys() | data2.keys())
    diff = []

    for k in keys:
        diff.append(get_diff(data1, data2, k))

    return diff


def get_diff(data1, data2, k):
    """Получает разницу для каждого ключа"""

    dict_ = {}
    data1_value = data1.get(k)
    data2_value = data2.get(k)

    if k in data1 and k not in data2:
        dict_['status'] = 'removed'
        dict_['old_value'] = data1_value

    elif k in data1 and k in data2:
        if data1_value == data2_value:
            dict_['status'] = 'unchanged'
            dict_["old_value"] = data1_value

        elif isinstance(data1_value, dict) and isinstance(data2_value, dict):
            dict_['status'] = 'nested'
            dict_['nested'] = get_diff_key(data1_value, data2_value, key=k)
        else:
            dict_['status'] = 'updated'
            dict_['old_value'] = data1_value
            dict_['new_value'] = data2_value

    elif k not in data1 and k in data2:
        dict_['status'] = 'added'
        dict_['new_value'] = data2_value

    child = dict([('key', k)])
    child.update(dict_)
    return child
