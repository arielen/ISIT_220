""" 6.	Вычислить n - количество точек, попадающих в круг радиуса R (R>0) с центром в начале координат. """

R = int(input('Введите радиус: '))
k = 0

for x in range(-R, R+1):  # range от r до r
    for y in range(-R, R+1):  # range от r до r
        if x ** 2 + y ** 2 <= R ** 2:
            k += 1
            print(k)