"""   Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ """

""" acc = list(input("Задайте точность для вычисления pi: "))

n = len(acc)-2

pi = round(sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n)), n)

print(pi) """

""" Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. """

""" num = int(input('Введите число: '))
def fac(n):
    delitor = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i 
            delitor.append(i)
        i += 1
    if n > 1:
        delitor.append(n)
    return delitor

print(fac(num)) """

""" Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. """

""" from random import randint
min = 1
max = 10
size = 20

my_list = [randint(min,max) for i in range(size)]

uniq_list =[]
for i in range(len(my_list)):
    count = 0
    for r in my_list:
        if my_list[i] == r: count +=1
    

print(f'Рандом:                {my_list}')
print(f'Ряд без повторений:    {set(my_list)}') """
