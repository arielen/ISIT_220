x = float(input('Введите ваше значение: '))

a = 2.8
b = -0.3
c = 4

if x < 1.5:
    z = a * (x ** 3) + b * x + c
elif x == 1.5:
    z = a / x + (x * (1 / 2)) + 1
else:
    z = (a + b * x) / x

print(f'Ваше значение функции равно:', '%.3f' % z)