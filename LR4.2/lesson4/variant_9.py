""" 9.	Начав тренировки, спортсмен в первый день пробежал 10 км.
Каждый следующий день он увеличивал дневную норму на 10% от нормы предыдущего дня.
Какой суммарный путь пробежит спортсмен за 7 дней?"""

distance = 10
procent = 0.1
sum_distance = 0

for day in range(1, 8):
    if day <= 7:
        sum_distance += distance
        distance += distance * procent
        day += 1

print(f'Ссумарно спортсмен за {day - 1} дней пробежит: {"%.3f" % sum_distance} км.')
