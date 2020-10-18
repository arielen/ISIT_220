import math

k = 2
x = 0.32
d = 1.25
a = 1
n = -4
b = 0.75
c = 2.2

y = 10 ** (-3) * math.tan(k * n) - ((x - a) * (x ** 2 + b ** 2)) / ((x ** 2 + b ** 2 + c * d) * (1 / 3)) - (
            math.cos(k * x) / math.sin(5))

print('Ваше число: ', '%.3f' % y)
