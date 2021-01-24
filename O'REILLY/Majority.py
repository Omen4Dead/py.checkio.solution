def is_majority(items: list) -> bool:
    # your code here
    t = 0
    f = 0

    try:
        for i in items:
            if i is True:
                t += 1
            else:
                f += 1
    except Exception as e:
        print(e)

    if t > f: return True
    elif t < f: return False
    else: return False


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
