from ._cart2_append import cart2_append
from ._tail import tail

def cartn_append(*list_of_lists: list) -> list:
    """Cartesian product of n lists.
    
    The difference from `cartn` is that the first element
    of the input `list_of_lists`
    is itself a list of lists.
    The elements from other lists
    are appended (inserted) to each sub-list of the first list.

    :param list list_of_lists(vararg): variable number of lists
    :return: a new list
    :rtype: list
      
    >>> cartn_append([['a','b'],['c','d']], [1,2], ['A','B'])
    [['a', 'b', 1, 'A'], ['a', 'b', 1, 'B'], ['a', 'b', 2, 'A'], ['a', 'b', 2, 'B'], ['c', 'd', 1, 'A'], ['c', 'd', 1, 'B'], ['c', 'd', 2, 'A'], ['c', 'd', 2, 'B']]
    """
    def aux(list_of_lists: list) -> list:
        if len(list_of_lists) == 0:
            return []
        elif len(list_of_lists) == 1:
            return list_of_lists[0]
        else:
            print(list_of_lists)
            return aux([cart2_append(list_of_lists[0], list_of_lists[1])] + tail(list_of_lists[1:]))
    
    return aux(list(list_of_lists))
