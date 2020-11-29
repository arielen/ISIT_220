i = 1
summa = 0
while i <= 10:
    formula = i / i + (i ** (1/2))
    summa += formula
    print(f'i={i}', '%.3f' % formula, '%.3f' % summa)
    i += 1
print('Сумма равна:', '%.3f' % summa)
