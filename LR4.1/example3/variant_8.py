import math

'''Вычислить в равностороннем треугольнике сторону, высоту, площадь,
 если радиус вписанной окружности равен r'''

r = float(input('Введите радиус вписанной окружности >>>  '))

S = 3 * math.sqrt(3) * r ** 2  # площадь равностороннего треугольника
h = r * 2 / 3  # высота равностороннего треугольника
a = math.sqrt(S / math.sqrt(3 / 4))  # сторона равностороннего треугольника

print('Сторона равностороннего треугольника: ' + str('%.3f' % a),
      'Высота равностороннего треугольника: ' + str('%.3f' % h),
      'Площадь равностороннего треугольника: ' + str('%.3f' % S), sep='\n')
