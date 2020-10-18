import math

a = -3.25
x = 8.2
k = 4
b = 0.05
d = 0.95

e = 2.71828

y = math.cos(k) * (x - a) + (math.fabs(x + a) * (1 / 5) / 2.4 * b) * e ** 3 + 10 ** (-4) * ((x + a) + x ** 4 + d) / (
            k * ((x - a) ** 3))

print('Ваше число: ', '%.3f' % y)
