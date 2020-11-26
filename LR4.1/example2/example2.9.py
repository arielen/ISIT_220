import math

a = 1.7
b = -1.25
c = -0.3
x = 2.5
k = 3

y = math.sqrt((a * b * c) / 2.4) - ((0.7 * a * b * c) / math.sin(7)) + (
            10 ** 4 * (math.fabs(math.cos(k * x)) * (1 / 5))) - ((math.fabs(b - a)) / (k * x))

print('Ваше число: ', '%.3f' % y)
