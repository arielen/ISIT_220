""" 6.	Определить, принадлежит ли точка М(x, y) внутренней области треугольника с вершинами
А(0, 0), В(а, 0), С(0, b), где а, b - положительные числа. """

x = int(input('Введите X: '))
y = int(input('Введите Y: '))
a = int(input('Введите a: '))
b = int(input('Введите b: '))
A = [0, 0]
B = [a, 0]
C = [0, b]

if x < B[0] and y < C[1]:
    print('Точка принадлежит внутренней области')
else:
    print('Точка НЕ принадлежит внутренней области')