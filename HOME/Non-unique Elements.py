# Your optional code here
# You can import some modules or create additional functions


def checkio(data: list) -> list:
    dictionary = {}

    for i in set(data):
        dictionary[i] = 0

    for j in data:
        dictionary[j] += 1

    d2 = dictionary.copy()
    for k in d2:
        if dictionary[k] == 1:
            dictionary.pop(k)

    a = list(dictionary.keys())

    for x in data[:]:
        if x not in a:
            data.remove(x)

    return data


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
