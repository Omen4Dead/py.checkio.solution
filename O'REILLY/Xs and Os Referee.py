"""
Крестики и Нолики - это игра для двух игроков (Х и О), которые расставляют эти знаки на 3х3 поле.
Игрок, который сумел разместить три своих знака в любой горизонтали, вертикали или диагонали -- выигрывает.
Но сейчас мы не будем играть в эту игру. Вы будете судить игру, и оценивать результат.
Вам дан результат игры, и вы должны решить, кто победил или что это ничья.
Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок.
В случае ничьи, результат должен быть "D".

Результаты игры представлены, как список (list) строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.
Вх. данные: Результат игры, как список (list) строк (str, unicode).
Вых. данные: "X", "O" или "D", как строка (str).
"""
from typing import List


def checkio(game_result: List[str]) -> str:
    for i in range(3):
        if game_result[i] == 'XXX':
            return 'X'
        elif game_result[i] == 'OOO':
            return 'O'
        elif game_result[0][i] == 'X' and game_result[1][i] == 'X' and game_result[2][i] == 'X':
            return 'X'
        elif game_result[0][i] == 'O' and game_result[1][i] == 'O' and game_result[2][i] == 'O':
            return 'O'
        elif game_result[0][0] == 'O' and game_result[1][1] == 'O' and game_result[2][2] == 'O':
            return 'O'
        elif game_result[0][0] == 'X' and game_result[1][1] == 'X' and game_result[2][2] == 'X':
            return 'X'
        elif game_result[0][2] == 'O' and game_result[1][1] == 'O' and game_result[2][0] == 'O':
            return 'O'
        elif game_result[0][2] == 'X' and game_result[1][1] == 'X' and game_result[2][0] == 'X':
            return 'X'
    return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
