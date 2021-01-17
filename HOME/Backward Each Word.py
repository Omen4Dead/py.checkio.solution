def backward_string_by_word(text: str) -> str:
    # your code here
    lst = []
    word = ''
    for i in text:
        if i != ' ':
            word = word + i
        else:
            lst.append(word)
            word = ''
            lst.append(i)
    else:
        lst.append(word)
    # print(lst)

    lst2 = []
    for j in lst:
        lst2.append(j[::-1])
    # print(lst2)
    res = ''.join(lst2)
    return res


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
