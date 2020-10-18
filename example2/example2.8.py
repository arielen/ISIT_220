import math

d = 1.2
x = 0.75
c = 1.3
i = 2
k = -3

y = (d * x - math.sqrt(math.fabs(c - d) / x)) ** 2 + 1.2 * math.tan(i) - 10 ** 3 * ((c - d) ** 2 / d * x) + (
    math.fabs(math.cos(k * x))) ** (1 / 3)

print('Ваше число: ', '%.3f' % y)
