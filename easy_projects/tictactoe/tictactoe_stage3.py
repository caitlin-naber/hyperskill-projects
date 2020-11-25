def bounding():
    print('---------')


def row_win(field, symbol, row):
    return [field[row][0], field[row][1], field[row][2]] == [symbol, symbol, symbol]


def col_win(field, symbol, col):
    return [field[0][col], field[1][col], field[2][col]] == [symbol, symbol, symbol]


def player_wins(field, symbol):
    top_across = row_win(field, symbol, 0)
    mid_across = row_win(field, symbol, 1)
    low_across = row_win(field, symbol, 2)
    left_down = col_win(field, symbol, 0)
    mid_down = col_win(field, symbol, 1)
    right_down = col_win(field, symbol, 2)
    left_diag = [field[0][0], field[1][1], field[2][2]] == [symbol, symbol, symbol]
    right_diag = [field[2][0], field[1][1], field[0][2]] == [symbol, symbol, symbol]
    return top_across or mid_across or low_across or left_down or mid_down or right_down or left_diag or right_diag


user_input = input('Enter cells:')

list_of_cells = list(user_input)
first_row = list_of_cells[0:3]
second_row = list_of_cells[3:6]
third_row = list_of_cells[6:9]
field = [first_row, second_row, third_row]

x_counter = 0
o_counter = 0
counter = 0
for i in list_of_cells:
    if i == '_':
        counter += 1
    if i == 'X':
        x_counter += 1
    if i == 'O':
        o_counter += 1


bounding()
print('| ' + first_row[0] + ' ' + first_row[1] + ' ' + first_row[2] + ' |')
print('| ' + second_row[0] + ' ' + second_row[1] + ' ' + second_row[2] + ' |')
print('| ' + third_row[0] + ' ' + third_row[1] + ' ' + third_row[2] + ' |')
bounding()


if player_wins(field, 'X') is True and player_wins(field, 'O') is True:
    print('Impossible')
elif abs(x_counter - o_counter) > 1:
    print('Impossible')
elif player_wins(field, 'X') is True:
    print('X wins')
elif player_wins(field, 'O') is True:
    print('O wins')
elif player_wins(field, 'X') is False and player_wins(field, 'O') is False and counter == 0:
    print('Draw')
elif player_wins(field, 'X') is False and player_wins(field, 'O') is False and counter >= 1:
    print('Game not finished')


