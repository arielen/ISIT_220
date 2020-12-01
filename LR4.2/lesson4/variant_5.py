""" 5.	sin(3)+sin(sin(3))+...+sin(sin(...sin(3))) """
import math as m

n = int(input('Введите колличество синусов: '))
sin = 3
summa = 0
for number in range(0, n):
    sin = m.sin(sin)
    summa += sin
print(summa)
