k = 1
summa = 0
while k <= 8:
    formula = 1 / k + (k + 1) ** 3
    summa += formula
    print(f'k={k}', '%.3f' % formula, '%.3f' % summa)
    k += 1
print('Сумма равна:', '%.3f' % summa)
