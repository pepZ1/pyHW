""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
 """
""" day = int(input("Введите день недели: "))

if 1 <= day <= 7:
     if day in [6, 7]:
         print("Отдыхай")
     else:
         print("Работать")
else:
     print("Такого дня недели нет!") """

""" Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). """


""" print('Введите координаты точки')

x = int(input('x= '))

y = int(input('y= '))

if x>0:

   if y>0:

       print('Точка лежит в 1 четверти')

   else:

       print('Точка лежит в 4 четверти')

else:

   if y>0:

       print('Точка лежит в 2 четверти')

   else:

       print('Точка лежит в 3 четверти') """

""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. """

""" def inputNumbers(x):
     xyz = ["X", "Y", "Z"]
     a = []
     for i in range(x):
         a.append(input(f"Введите значение {xyz[i]}: "))
     return a


def checkPredicate(x):
     left = not (x[0] or x[1] or x[2])
     right = not x[0] and not x[1] and not x[2]
     result = left == right
     return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
     print(f"Утверждение истинно")
else:
     print(f"Утверждение ложно") """

""" Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). """

""" quart_number = int(input())

if quart_number in [1, 2, 3, 4]:
     if quart_number == 1:
         print("Значения координат точки: х ∈ [1, ∞), y ∈ [1, ∞)")
     elif quart_number == 2:
         print("Значения координат точки: х ∈ [-1, -∞), y ∈ [1, ∞)")
     elif quart_number == 3:
         print("Значения координат точки: х ∈ [-1, -∞), y ∈ [-1, -∞)")
     elif quart_number == 4:
         print("Значения координат точки: х ∈ [1, ∞), y ∈ [-1, -∞)")
else:
     print("!Введите число от 1 до 4!") """


""" Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 """

def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Только целые числа")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Расстояние: {format(calculateLengthSegment(pointA, pointB), '.2f')}")