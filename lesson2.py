import math

a = 1.7
b = -1.25
c = -0.3
x = 2.5
k = 3

first = math.sqrt((a * b * c) / 2.4)

second = (0.7 * (a * b * c)) / math.sin(7)

third = 10**4 * pow(math.cos(math.fabs(k * x)), (1/5))

fourth = math.fabs(b - a) / (k * x)

y = first - second + third - fourth

print(y)
print(first, second, third, fourth)



