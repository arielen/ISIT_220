""" 10.	Начав тренировки, спортсмен в первый день пробежал 10 км.
Каждый следующий день он увеличивал дневную норму на 10% от нормы предыдущего дня.
Через сколько дней спортсмен будет пробегать в день 20 км? """

distance = 10
next_day = 0.1
day = 1
for distance in range(10, 20):
    if distance < 20:
        distance += distance * next_day
        day += 1
print(f'Через {day} дней спортсмен будет пробегать: {"%.3f" % distance} км в день.')