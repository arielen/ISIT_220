import math

a = 4.72
b = 1.25
d = -0.01
x = 2.25
i = 2
k = 3

y = (a * x ** 2 + math.fabs(d)) / (a + b) ** 2 - 10 ** 4 * ((k * x) / (a + b) ** 2) * (1 / 5) - (
            math.cos(i) / math.sin(k * x))

print('Ваше число: ', '%.3f' % y)
