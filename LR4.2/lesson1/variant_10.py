x = float(input('Введите ваше число X: '))

a = 2.5

if x < a:
    y = x ** 2 + x ** 3
elif x == a:
    y = x * a - x
else:
    y = (a * (1 / 2)) + 2 * x

print(f'Ваше значение функции равно:', '%.3f' % y)
