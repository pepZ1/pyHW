""" Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
 """
arr = [2,3,5,9,3]
sum = 0
for i in range(1, len(arr), 2):
    sum += arr[i]

print(sum)
