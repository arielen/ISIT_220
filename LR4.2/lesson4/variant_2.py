""" 2.	Дана последовательность из N чисел.
Выведите значение наименьшего из всех положительных нечётных элементов в последовательности.
Если таких элементов нет – выведите NO. """
    
massive = [6, 9, 5, 9, 9, 11, 9, 13, 9]
number_min = float('+inf')  # присваиваем числу бесконечность
found = False

for number in massive:
    if number % 2 == 1:
        if number < number_min:
            number_min = number
            number += 1
            found = True
    else:
        number += 1

if found is True:
    print('Наименьшее число: ', number_min)
else:
    print('NO')
