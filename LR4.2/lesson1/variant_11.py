x = float(input('Введите ваше число X: '))

a = 1.65

if x > 1.4:
    Q = a * (x ** 3) - (7 / (x ** 2))
elif x == 1.4:
    Q = a * x - (x * (1 / 2)) + 1
else:
    Q = x - 7

print(f'Ваше значение функции равно:', '%.3f' % Q)
