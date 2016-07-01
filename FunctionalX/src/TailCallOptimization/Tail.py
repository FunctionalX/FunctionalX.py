"""Tail

`Tail` class will wrap the returned recursive function into
an object.

>>> Tail(target_function, args)
"""
class Tail(object):
    def __init__(self, target_function, *args, **kwargs):
        self.function = target_function
        self.args = args
        self.kwargs = kwargs

    def eval(self):
        return self.function(*self.args, **self.kwargs)