import math

a = -2.5
b = 1.35
x = 2.75
i = 3
c = -0.72

y = (1.5 * (a - b) ** 2) / math.fabs(a - b) * c + i / 5 + 10 ** 3 * math.sqrt(math.fabs(a - b)) - (
            2.5 * (a + x ** 2) * math.sin(7)) / (i * x ** 2 + a ** 2 * b * c)

print('Ваше число: ', '%.3f' % y)
