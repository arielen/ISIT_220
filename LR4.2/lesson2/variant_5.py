i = 2
summa = 1
while i <= 10:
    formula = ((i + 1) / (i + 2)) + (i / i)
    summa *= formula
    print(f'i={i}', '%.3f' % formula, summa)
    i += 1
print('Сумма равна:', '%.3f' % summa)
