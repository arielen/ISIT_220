"""Вычислить высоту треугольника со сторонами а, b и c"""

a = float(input('Введите сторону a >>>  '))
b = float(input('Введите сторону b >>>  '))
c = float(input('Введите сторону c >>>  '))

h_a = b * c / a
h_b = a * c / b
h_c = a * b / c

print('Высота a равна: ' + str('%.3f' % h_a), 'Высота b равна: ' + str('%.3f' % h_b),
      'Высота c равна: ' + str('%.3f' % h_c), sep='\n')