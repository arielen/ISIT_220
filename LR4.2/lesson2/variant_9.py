import math as m

k = 1
summa = 1
while k <= 5:
    formula = (1 / (2 * k + 1) ** 2) + k / m.factorial(k)
    summa *= formula
    k += 1
print('Произведение равно:', '%.3f' % summa)
