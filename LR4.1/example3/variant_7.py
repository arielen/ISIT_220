import math

'''Вычислить площадь правильного 6-угольника,
описанного около круга радиусом R'''

R = float(input('Введите радиус круга >>>  '))
s = (3 * math.sqrt(3) * R ** 2) / 2

print('Площадь шестиуголника: ' + '%.3f' % s)