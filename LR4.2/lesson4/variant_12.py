""" 12.	Водяной паук серебрянка строит в воде воздушный домик, перенося на лапках и
брюшке пузырьки атмосферного воздуха, а затем помещая их под купол паутины.
Сколько рейсов надо сделать пауку, чтобы построить домик объемом 1 куб. см, если каждый раз он берет 5 куб. мм воздуха?
Давлением воды пренебречь """

flight = 0

for volume in range(1):
    while volume <= 1:
        volume += 0.005  # 1куб.мм. = 0,001куб.см
        flight += 1

print(f'Пауку потребуется {flight} рейсов, чтобы построить домик объемом {"%.0f" % volume} куб. см')