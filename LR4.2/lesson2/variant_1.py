i = 1
summa = 0
while i <= 10:
    formula = (1 / (i ** 2)) + 2 * i
    summa += formula
    print(f'i={i}', '%.3f' % formula, 'ссумма с предыдущим', '%.3f' % summa)
    i += 1
print('Сумма равна:', '%.3f' % summa)
