""" 5. Реализуйте алгоритм перемешивания списка. """
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Updated with sum Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11 

number = input('Введите вещественное число: ')
sum = 0
for i in range(len(number)):
      if number[i] != ',':
          sum += int(number[i])

print(f'{number} -> {sum}')




""" 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. """
summa = 0
for i in range(1, int(input()) + 1):
    summa += ((1 + 1 / i) ** i)
print(round(summa))

""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")

