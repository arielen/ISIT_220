i = 1
summa = 0
while i <= 10:
    formula = (1 / (i ** 4)) + i
    summa += formula
    print(f'i={i}', '%.3f' % formula, summa)
    i += 1
print(f'Сумма равна: {summa}')
