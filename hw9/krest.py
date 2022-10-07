pole = list(range(1, 10))

def draw_pole(pole):
    print('-------------')
    for i in range(3):
        print(f'| {pole[i*3]} | {pole[1+i*3]} | {pole[2+i*3]} |')
        print('-------------')

def choice_input(player_choice):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_choice+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print('Введите число от 1 до 9')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(pole[player_answer-1]) not in 'XO'):
                pole[player_answer-1] = player_choice
                valid = True
            else:
                print('ЗАНЯТО!')
        else:
            print('От 1 до 9!')

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main_def(board):
    counter = 0
    win = False
    while not win:
        draw_pole(board)
        if counter % 2 == 0:
            choice_input('X')
        else:
            choice_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(f'{tmp}, выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    draw_pole(board)

main_def(pole)