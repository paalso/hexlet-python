def function_with_exception(arg):
    if arg == 0:
        raise ValueError('Arg is 0')
    return arg * 13
