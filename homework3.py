""" Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
 - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
 """
""" arr = [2,3,5,9,3]
sum = 0
for i in range(1, len(arr), 2):
    sum += arr[i]

print(sum) """

""" Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """

""" arr = list(map(int, input("Введите числа через пробел:\n").split()))

def mult(lst):
    new_lst = []
    if len(lst) % 2 != 0:
        num_par = len(lst)//2 + 1 
    else: 
        num_par = len(lst)//2
    
    for i in range(num_par):
        new_lst.append(lst[i]*lst[len(lst)-i-1])
    return new_lst

print(f'Произведения пар чисел: {mult(arr)}') """

""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

""" def bin(n):
    s = ''
    while n > 0:
        s = str(n%2) + s
        n //= 2
    return s
 
while 1:
    n = int(input('Введите число: '))
    if n != 0:
        print(bin(n))
    else:
        break
 """

""" Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

""" arr = [1.1, 1.2, 3.1, 5, 10.01]

frac_part = []

for i in arr:
    if i%1 != 0:
        frac_part.append(round(i%1,2))

print(max(frac_part)-min(frac_part)) """

""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """

num = int(input('Введите число: '))

neg_num = - num

Fibo = []

def FibMinus(n):
    if n == -1: return 1
    elif n == -2: return -1
    return FibMinus (n + 2) - FibMinus (n + 1) 

def FibPlus(n):
    if n in [1,2]:
        return 1
    elif n == 0:
        return 0
    else:
        return FibPlus(n-1) + FibPlus(n-2)

for i in range(neg_num, num + 1):
    if i < 0:
        Fibo.append(FibMinus(i))
    else:
        Fibo.append(FibPlus(i))    

print(Fibo)

