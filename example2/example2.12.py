import math

a = 0.02
x = -3.25
b = 2.5
c = 1.2
d = 0.5
k = 6

e = 2.71828

y = (math.fabs(a * x - b) ** 3 + math.fabs(a - b) - e ** (k * d)) / (10 ** 4 * d ** 5 + b ** 2 + c) - math.sin(2) + (
            d + b) ** (1 / 5)

print('Ваше число: ', '%.3f' % y)
