import os


def _right(coll, path, value):
    length = len(path)
    last_index = length - 1
    index = 0
    nested = coll

    while index < length:
        key = path[index]
        new_value = value
        if index != last_index:
            obj_value = nested[key] if key in nested else None
            new_value = obj_value if isinstance(obj_value, dict) else {}
        nested[key] = new_value
        nested = nested[key]
        index += 1
    return coll


def _wrong1(coll, path, value):
    length = len(path)
    last_index = length - 1
    index = 0
    nested = coll

    while index < length:
        key = path[index]
        new_value = value
        if index != last_index:
            obj_value = nested[key] if key in nested else None
            new_value = obj_value if isinstance(obj_value, dict) else {}
        nested[key] = new_value
        nested = nested[key]
        index += 1
    coll['key'] = 'value'
    return coll


def _wrong2(coll, path, value):
    length = len(path)
    last_index = length - 1
    index = 0
    nested_coll = coll

    while index < length:
        key = path[index]
        new_value = value
        if index != last_index:
            new_value = {}
        nested_coll[key] = new_value
        nested_coll = nested_coll[key]
        index += 1
    return coll


def _wrong3(coll, path, value):
    if not path:
        return coll
    key = path[0]
    coll[key] = value
    return coll


functions = {
    "right": _right,
    "wrong1": _wrong1,
    "wrong2": _wrong2,
    "wrong3": _wrong3,
}


def get_function(func_alias):
    return functions[func_alias]


##def get_function():
##    name = os.environ['FUNCTION_VERSION']
##    return functions[name]
