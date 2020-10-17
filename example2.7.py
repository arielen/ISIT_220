import math

k = -2
a = 3.5
b = 0.35
x = 1.523

e = 2.71828  # исходя из интернета

y = 10 ** 4 * (a * x) / b ** 2 - math.fabs((a - b) / (k * x)) + (math.log1p(3) / (a * x + b ** 2) ** (1 / 3)) - e ** (
        -k * x)

print('Ваше число: ', '%.3f' % y)
