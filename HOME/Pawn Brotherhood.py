columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
lines = ['1', '2', '3', '4', '5', '6', '7', '8']


def safe_pawns(pawns: set) -> int:
    safe_sum = 0
    for figure in pawns:
        index_figure_l = lines.index(figure[1])  # индекс цифры координаты фигуры
        if index_figure_l == 0:
            continue

        defender_left = ''
        defender_right = ''

        index_figure_col = columns.index(figure[0])  # индекс буквы координаты фигуры
        if index_figure_col == 7:
            defender_left = columns[index_figure_col - 1] + lines[index_figure_l - 1]
        if index_figure_col == 0:
            defender_right = columns[index_figure_col + 1] + lines[index_figure_l - 1]
        if index_figure_col != 7 and index_figure_col != 0:
            defender_left = columns[index_figure_col - 1] + lines[index_figure_l - 1]
            defender_right = columns[index_figure_col + 1] + lines[index_figure_l - 1]

        if defender_left in pawns:
            safe_sum += 1
            continue
        if defender_right in pawns:
            safe_sum += 1

    return safe_sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")