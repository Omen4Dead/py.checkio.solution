"""
Create and return a new iterable that contains the same elements as the argument iterable items,
but with the reversed order of the elements inside every maximal strictly ascending sublist.
This function should not modify the contents of the original iterable.

Input: Iterable
Output: Iterable
Precondition: Iterable contains only ints

The mission was taken from Python CCPS 109 Fall 2018.
It’s being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
"""


def reverse_ascending(items):
    new_items = items.copy()
    spam = []
    while len(new_items) > 0:
        ind = 1
        while ind < len(new_items):
            if new_items[ind - 1] >= new_items[ind]:
                spam.append(new_items[:ind])
                new_items = new_items[ind:]
                ind += 1
                break
            else:
                ind += 1
        else:
            spam.append(new_items[:])
            new_items.clear()

    print(spam)
    eggs = []

    for i in spam:
        i.sort(reverse=True)
        eggs = eggs + i

    print(eggs)
    return eggs


if __name__ == '__main__':
    print("Example:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
