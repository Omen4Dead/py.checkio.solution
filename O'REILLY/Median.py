"""
Медиана — это числовое значение, которое делит сортированый массив чисел на нижнюю и верхнюю половины.
В сортированом массиве с нечётным числом элементов медиана — это число в середине массива.
Для массива с чётным числом элементов, где нет одного элемента точно посередине, медиана — это среднее значение
двух чисел, находящихся в середине массива. В этой задаче дан непустой массив натуральных чисел.
Вам необходимо найти медиану данного массива.

Входные данные: Массив как список (list) чисел (int).

Выходные данные: Медиана как число (int, float).
"""
from typing import List


def checkio(data: List[int]) -> [int, float]:
    # replace this for solution
    data.sort()
    res = len(data) // 2
    if len(data) % 2 == 0:
        return (data[res - 1] + data[res]) / 2
    else:
        return data[res]

    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")
