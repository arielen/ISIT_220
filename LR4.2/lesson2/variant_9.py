k = 1
summa = 1
while k <= 5:
    formula = (1 / (2 * k + 1) ** 2) + k / k
    summa *= formula
    print(f'k={k}', '%.3f' % formula, summa)
    k += 1
print('Сумма равна:', '%.3f' % summa)
