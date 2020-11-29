i = 1
summa = 1
while i <= 10:
    formula = i / ((2 * i) ** 2)
    summa *= formula
    print(f'i={i}', '%.3f' % formula, summa)
    i += 1
print(f'Сумма равна: {summa}')
