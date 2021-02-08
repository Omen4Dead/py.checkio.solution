"""
Ваше задание - пересортировать список, расположив числа в порядке уменьшения их количества в списке.
Если несколько чисел встречаются одинаково часто - их необходимо расположить в порядке от меньшего к большему,
вне зависимости от того, в каком порядке они встречаются в исходном списке.
Например: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]
"""
from collections import Counter


def frequency_sorting(numbers):
    # replace this for solution
    numbers.sort()
    counter = Counter(numbers)
    print(counter.most_common())
    result = []

    for num, count in counter.most_common():
        for i in range(count):
            result.append(num)

    print(result)
    return result


if __name__ == '__main__':
    print("Example:")

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")
