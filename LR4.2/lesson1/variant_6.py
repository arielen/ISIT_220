x = float(input('Введите ваше число X: '))

a = 2.5

if x > a:
    y = x ** 2 + x ** 4 - a
elif x == a:
    y = x * a + (x * (1 / 2))
else:
    y = a + 2 * x

print(f'Ваше значение функции равно:', '%.3f' % y)
