from test1 import origin_func as original


def func(a, b):
    return a + b


def base_func():
    return original()
