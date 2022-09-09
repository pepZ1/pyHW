""" N = int(input('Введите количество чисел больше 0: '))

a = 1
res = 1

print (res)
while a < N:
   res = res*(-3)
   a += 1
print (res) """
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)