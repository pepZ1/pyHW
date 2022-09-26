""" Напишите программу, удаляющую из текста все слова, содержащие ""абв"". """

""" word = 'Сначала я абв как абвпонял, а потом понял!'
find = 'абв'


def del_words(letters, del_text):
    letters = list(filter(lambda x: del_text not in x, letters.split()))
    return " ".join(letters)
print(del_words(word, find)) """

""" Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом"" """

""" from random import randint

player1 = input('Игрок 1 представьтесь: ')
player2 = input('Игрок 2 представьтесь: ')
quant_cand = 2021
max_take_cand = 28



def takes_candys(name):
    x = int(input(f"{name}, введите количество конфет 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, количество должно быть от 1 до 28: "))
    return x

priority = randint(0,1)

if priority:
    print(f'Первым ходит: {player1}')
else:
    print(f'Вторым ходит: {player2}')

while quant_cand > max_take_cand:
    if priority:
        num_cand = takes_candys(player1)
        quant_cand -= num_cand
        priority = False
        print(f'{player1} взял(а) {num_cand}, на столе осталось {quant_cand} шт')
    else:
        num_cand = takes_candys(player2)
        quant_cand -= num_cand
        priority = True
        print(f'{player2} взял(а) {num_cand}, на столе осталось {quant_cand} шт')

if priority:
    print(f'Победа за {player1}')
else:
    print(f'Победа за {player2}') """

"""vs bot"""

""" from random import randint

player1 = input('Введите Ваше имя: ')
player2 = 'Automaton3000'
quant_cand = 140
max_take_cand = 28

def takes_candys(name):
    x = int(input(f"{name}, введите количество конфет 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, количество должно быть от 1 до 28: "))
    return x

def calc_for_bot(quant):
    q = randint(1, 29)
    if quant > 56:
        while (quant - q)%28 != 0:
            q = randint(1, 28)
    else:
            q = quant - 29
    if q == 0:
        q = 1
    return q

priority = randint(0,1)

if priority:
    print(f'Первым ходит: {player1}')
else:
    print(f'Первым ходит: {player2}')

while quant_cand > max_take_cand:
    if priority:
        num_cand = takes_candys(player1)
        quant_cand -= num_cand
        priority = False
        print(f'{player1} взял(а) {num_cand}, на столе осталось {quant_cand} шт')
    else:
        num_cand = calc_for_bot(quant_cand)
        quant_cand -= num_cand
        priority = True
        print(f'{player2} взял(а) {num_cand}, на столе осталось {quant_cand} шт')

if priority:
    print(f'Победа за {player1}')
else:
    print(f'Победа за {player2}') """

""" Создайте программу для игры в ""Крестики-нолики"". """


""" pole = list(range(1, 10))

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

main_def(pole) """

""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. """

def Compression(text): #алгоритм сжатия
    compresdata = ''

    i = 0
    while i < len(text):
     count = 1
    while i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
        i += 1
    compresdata += str(count) + text[i]
    i += 1

    return compresdata


def Recovery(text): #алгоритм восстановления
    datarecovery = ''

    i = 0
    while i < len(text):
        datarecovery += str(text[i+1]) * int(text[i])
        i+=2

    return datarecovery


with open('Text1.txt', 'r') as t1:
    t1 = t1.read()

with open('Text2.txt', 'w+') as t2:
    t2.write(Compression(t1))
    t2.seek(0) #возврат курсора на начало строки
    t2 = t2.read()

with open('Text3.txt', 'w') as t3:
    t3.write(Recovery(t2))
