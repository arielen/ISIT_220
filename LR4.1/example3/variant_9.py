import math

'''Дана сторона равностороннего треугольника.
 Найти площадь этого треугольника'''

a = float(input('Введите сторону равностороннего треугольника >>>  '))

S = (math.sqrt(3) * a ** 2) / 4  # площадь равностороннего треугольника

print('Площадь равностороннего треугольника: ' + str('%.3f' % S))
