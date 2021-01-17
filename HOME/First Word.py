import string


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    punctuation = string.punctuation + '\u2014\u2013\u2012\u2010\u2212' + '«»‹›‘’“”„`'
    for i in punctuation:
        text = text.strip(i)
    text = text.replace('.', ' ').replace(',', ' ')

    words = text.split()
    return words[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
