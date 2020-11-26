i = int(input('Введите число, для решения функции: '))

a = 2.1
b = 1.8
c = -20.5

if i >= 6:
    z = a / i + b * (i ** 2) + c
elif 4 < i < 6:
    z = i
else:
    z = a * i + b * i

print(f'Ваше значение:', '%.3f' % z)
