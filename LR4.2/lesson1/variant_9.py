x = float(input('Введите ваше значение X: '))

t = 2.2

if x > 0.5:
    z = (x ** 3) + 1
elif x == 0.5:
    z = x + 1 / x
else:
    z = (x - t) * (x * (1 / 2))

print(f'Ваше значение функции равно:', '%.3f' % z)