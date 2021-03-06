""" 11.	Определить суммарный объем в метрах 12 вложенных друг в друга шаров со стенками 5 мм.
Внутренний диаметр внутреннего шара равен 10 см.
Считать, что шары вкладываются друг в друга без зазора. """
import math as m

D = 10
wall = 5
ball = 12
all_volume = 0
# следует найти объем следующх (вложенных)
for balls in range(1, 13):
    if balls <= 12:
        volume = (4 / 3) * m.pi * (D / 2) ** 3  # объем первого шара
        all_volume += volume  # накопитель сумм
        print(balls, volume, all_volume)
        D += 0.5  # увеличиваем шар со стенками

print(f'Ссумарный объем, составляет: {"%.0f" % (all_volume // 100)} метров '
      f'{"%.0f" % (all_volume % 100)} сантиметров')
