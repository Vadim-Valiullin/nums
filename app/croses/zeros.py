
board = list(range(1, 10))

def draw(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[ 0 + i *3], '|', board[ 1 + i *3], '|', board[ 2 + i *3], '|')
        print('-' * 13)

def turn(player, symb):
    while True:
        player_turn = input(f'{player}, куда ставим {symb}? ')
        try:
            player_turn = int(player_turn)
        except:
            print('Введите число!')
            continue

        if player_turn >= 1 and player_turn <= 9:
            if type(board[player_turn - 1]) is int:
                board[player_turn - 1] = symb
                break
            else:
                print('Эта клетка занята!')
        else:
            print('Число от 1 до 9!')

def check(board):
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for var in win:
        if board[var[0]] == board[var[1]] == board[var[2]]:
            return board[var[0]]
    return False

def main():
    name_player_1 = input('Имя первого игрока: ')
    name_player_2 = input('Имя второго игрока: ')
    turn_counter = 0
    while True:
        draw(board)
        if turn_counter % 2 == 0:
            turn(name_player_1, 'X')
        else:
            turn(name_player_2, 'O')
        turn_counter += 1

        if turn_counter > 4:
            win = check(board)
            if win:
                if win == 'X':
                    print(f'Игрок {name_player_1} победил!')
                    draw(board)
                else:
                    print(f'Игрок {name_player_2} победил!')
                    draw(board)
                break
        if turn_counter == 9:
            print('Ничья!')
            break

main()

