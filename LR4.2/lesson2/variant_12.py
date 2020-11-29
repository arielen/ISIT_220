i = 1
summa = 0
while i <= 5:
    formula = ((100 / (i ** (1 / 2))) + i)
    summa += formula
    print(f'i={i}', '%.3f' % formula, '%.3f' % summa)
    i += 1
print('Сумма равна:', '%.3f' % summa)
