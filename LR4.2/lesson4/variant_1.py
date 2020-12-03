""" 1.	Дана последовательность из N чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет – выведите NO. Если таких пар соседей несколько - выведите первую пару.  """

massive = [1, 2, 3, 4, 5, 6, 7, 8, 8]
number_next = 0
found = False

for number in massive:
    if number == number_next * (-1) or number == number_next:
        found = True
        print(f'Одинаковые числа: {number} и {number_next}')
        break
    else:
        number_next = number
        number += 1

if found is False:
    print('NO')