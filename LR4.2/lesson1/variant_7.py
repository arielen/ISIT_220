x = float(input('Введите ваше число: '))

t = 2.2

if x < 0.5:
    z = x ** 2 / (-x + t)
elif x == 0.5:
    z = x + t + 1 / x
else:
    z = (x + t) * (x * (1 / 2))

print(f'Ваше значение функции равно:', '%.3f' % z)
