"""
Given an iterable of ints , create and return a new iterable whose first two elements are the same as in items,
after which each element equals the median of the three elements in the original list ending in that position.
"""
from typing import Iterable


def median_three(els):
    # your code here
    if len(els) < 3:
        return els
    spam = [els[0], els[1]]
    count = 2
    while count < len(els):
        a = els[count - 2:count + 1]
        a.sort()
        spam.append(a[1])
        count += 1

    return spam


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
