i = 1
summa = 1
while i <= 10:
    formula = (1 / i) + i ** 3
    summa *= formula
    print(f'i={i}', '%.3f' % formula, summa)
    i += 1
print('Сумма равна:', '%.3f' % summa)
