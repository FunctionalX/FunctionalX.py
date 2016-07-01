"""Tail

`Tail` class will wrap the returned recursive function into
an object.

>>> Tail(target_function, args)
"""
class Tail(object):
    def __init__(self, target_function, *args, **kwargs):
        self.target = target_function
        self.args = args
        self.kwargs = kwargs

    def eval(self):
    	if hasattr(self.target, "call"):
    		return self.target.call(*self.args, **self.kwargs)
    	else:
        	return self.target(*self.args, **self.kwargs)