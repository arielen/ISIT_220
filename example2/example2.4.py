import math

a = 1.52
b = -13.2
n = 4
x = 1.4

y = 0.5 * ((a ** 2 * x + math.fabs(b)) / (a + b) ** 2 - b) + (math.sin(x) / math.cos(n * x)) + 10 ** 4 * (
            a ** 2) ** 1 / 5

print('Ваше число: ', '%.3f' % y)
