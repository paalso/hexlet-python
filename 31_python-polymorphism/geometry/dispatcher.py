# dispatcher.py

_virtual_table = {}


def defmethod(type_name, method_name, fn):
    if type_name not in _virtual_table:
        _virtual_table[type_name] = {}
    _virtual_table[type_name][method_name] = fn
    print(f'_virtual_table:\n{_virtual_table}')


def call(obj, full_method_name, args):
    type_name = obj['name']
    # method_name = full_method_name
    method_name = full_method_name.split('.')[-1]
    
    fn = _virtual_table.get(type_name, {}).get(method_name)

    _introspect_call(_virtual_table, type_name, full_method_name, method_name, fn)
    
    if not fn:
        return None
    return fn(obj, *args)


def _introspect_call(
        _virtual_table, type_name, full_method_name, method_name, fn):
    print('\nIntrospecting call:')
    print(f'type_name: {type_name}')
    print(f'full_method_name: {full_method_name}')
    print(f'method_name: {method_name}')
    print(f'fn: {fn}')
    print(f'_virtual_table:\n{_virtual_table}')
    print('--------------------------------------------\n')
