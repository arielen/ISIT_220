import math

a = 3.5
b = -0.7
i = 2
x = 0.8

first_example = 10**4 * math.sin(a) - (0.32 * x**3 + 4 * x + b)/(math.cos(i * a))
second_example = (0.32 * x**3 - b)*(1/5) + math.fabs(b)

print(first_example - second_example)
