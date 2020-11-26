import math

"""В равнобедренном треугольнике боковая сторона a см, а основание b см.
Найти высоту, опущенную на основание"""

a = float(input('Введите сторону a >>>  '))
b = float(input('Введите сторону b >>>  '))

h_a = math.sqrt(b ** 2 - (a ** 2 / 4))
h_b = math.sqrt(a ** 2 - (b ** 2 / 4))

print('Высота опущенная на основание а: ' + str('%.3f' % h_a),
      'Высота опущенная на основание b: ' + str('%.3f' % h_b), sep='\n')
