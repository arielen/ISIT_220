x = float(input('Введите ваше число: '))

a = 1.5

if x > 1.3:
    y = x ** 2 - 7 / x
elif x == 1.3:
    y = a * x + 7 - x
else:
    y = x ** 2 + 7 - x

print(f'Ваше значение функции равно:', '%.3f' % y)
