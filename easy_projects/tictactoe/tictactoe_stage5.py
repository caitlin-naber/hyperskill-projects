def print_matrix(field):
    print('---------')
    print('| ' + field[0][0] + ' ' + field[0][1] + ' ' + field[0][2] + ' |')
    print('| ' + field[1][0] + ' ' + field[1][1] + ' ' + field[1][2] + ' |')
    print('| ' + field[2][0] + ' ' + field[2][1] + ' ' + field[2][2] + ' |')
    print('---------')


def get_game_state(board_state, field):
    if player_wins(field, 'X') is True and player_wins(field, 'O') is True:
        board_state = 'Impossible'
    elif abs(x_counter - o_counter) > 1:
        board_state = 'Impossible'
    elif player_wins(field, 'X') is True:
        board_state = 'X wins'
    elif player_wins(field, 'O') is True:
        board_state = 'O wins'
    elif player_wins(field, 'X') is False and player_wins(field, 'O') is False and empty_counter == 0:
        board_state = 'Draw'
    elif player_wins(field, 'X') is False and player_wins(field, 'O') is False and counter >= 1:
        board_state = 'Game not finished'
    return board_state


def coord_list(coordinates):
    coord_list = coordinates.split()
    return coord_list


def check_numeric(coordinates):
    coord_list_var = coord_list(coordinates)
    coords = ''.join(coord_list_var)
    if coords.isnumeric() is False:
        print('You should enter numbers!')
        return True


def check_values(coordinates):
    coord_list_var = coord_list(coordinates)
    counter = 0
    for item in coord_list_var:
        coord_list_var[counter] = int(item)
        counter += 1
    if coord_list_var[0] < 1 or coord_list_var[0] > 3 or coord_list_var[1] < 1 or coord_list_var[1] > 3:
        print('Coordinates should be from 1 to 3')
        return True
    else:
        return coord_list


def check_cells(field, coordinates):
    coord_list_var = coord_list(coordinates)
    x = coord_list_var[0]
    y = coord_list_var[1]
    a = 3 - int(y)
    b = int(x) - 1
    if field[a][b] == '_':
        if round % 2 == 0:
            field[a][b] = 'O'
        else:
            field[a][b] = 'X'
    else:
        print('This cell is occupied! Choose another one!')
        return True


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

list_of_cells = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
first_row = list_of_cells[0:3]
second_row = list_of_cells[3:6]
third_row = list_of_cells[6:9]
field = [first_row, second_row, third_row]

round = 1
x_counter = 0
o_counter = 0
counter = 0
empty_counter = 9

for i in list_of_cells:
    if i == '_':
        counter += 1
    if i == 'X':
        x_counter += 1
    if i == 'O':
        o_counter += 1

game_state = 'Game not finished'
while game_state == 'Game not finished':
    game_state = get_game_state(game_state, field)
    print_matrix(field)
    if game_state != 'Game not finished':
        print(game_state)
        break
    else:
        coordinates = input('Enter the coordinates:')
        while check_numeric(coordinates) is True or check_values(coordinates) is True or \
                check_cells(field, coordinates) is True:
            coordinates = input('Enter the coordinates:')
        get_game_state(game_state,field)
        round += 1
        empty_counter -= 1