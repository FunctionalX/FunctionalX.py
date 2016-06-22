"""
Return the rest of the list (beyond the first element).
If the input list is empty or has only one element, then return `[]`.

Usage: others(list1)
Author: Yuhang(Steven) Wang
Date: 06/21/2016
"""
def tail(list1: list) -> list:
    if len(list1) <= 1:
        return []
    else:
        return list1[1:]
