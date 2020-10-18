import math

k = 3
a = 3.5
b = 0.35
n = 4
x = -0.02

y = (((a * b * x) + math.tan(2 * k)) / (math.fabs(a - b) + 0.5 * x)) - (
            10 ** 4 * x * (math.sin(n * a) / math.cos(k * x))) + ((a * b * x) / ((a - b) * (1 / 3)))

print('Ваше число: ', '%.3f' % y)
