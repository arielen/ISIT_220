import math

"""Треугольник задан тремя сторонами.
Вычислить его медианы"""

a = float(input('Введите сторону "a" >>>  '))
b = float(input('Введите сторону "b" >>>  '))
c = float(input('Введите сторону "c" >>>  '))

median_a = 1 / 2 * math.sqrt(2 * b ** 2 + 2 * c ** 2 - a ** 2)
median_b = 1 / 2 * math.sqrt(2 * a ** 2 + 2 * c ** 2 - b ** 2)
median_c = 1 / 2 * math.sqrt(2 * a ** 2 + 2 * b ** 2 - c ** 2)

print('Медиана А = ' + str('%.3f' % median_a), 'Медиана B = ' + str('%.3f' % median_b),
      'Медиана C = ' + str('%.3f' % median_c), sep='\n')
