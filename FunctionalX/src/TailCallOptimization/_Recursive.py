from ._Tail import Tail
"""Recursive

A wrapper class to used for transforming recursive functions 
into nested functions.

>>> @Recursive
    def f(n):
        if n == 0:
            return n
        else:
            return f(n-1)

To use the function `f`, just use the regular python
call syntax:

>>> f(10)
0
"""
class Recursive(object):
    def __init__(self, target_recursive_function):
        self.function = target_recursive_function

    def __call__(self, *args, **kwargs):
        value = self.function(*args, **kwargs)
        while type(value) is Tail:
            value = value.eval()
        return value
