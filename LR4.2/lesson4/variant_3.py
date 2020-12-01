""" 3.	Дана последовательность чисел, упорядоченная по возрастанию элементов в ней.
Определите, сколько в ней различных элементов. """

massive = [1, 2, 3, 3, 3, 3, 3, 3, 4, 6, 6, 7, 8, 9]
element_max = float('-inf')  # присваиваем минус бесконечность
other_element = 0

for element in massive:
    if element != element_max and element > element_max:
        other_element += 1
        element_max = element
print('Разных элементы: ', other_element)
