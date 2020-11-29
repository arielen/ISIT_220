""" 2.	Программа упорядочивает три введенных числа по возрастанию. """

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))

if number1 > number2 and number1 > number3:
    if number2 > number3:
        print(number1, number2, number3)
    else:
        print(number1, number3, number2)
elif number2 > number1 and number2 > number3:
    if number1 > number3:
        print(number2, number1, number3)
    else:
        print(number2, number3, number1)
else:
    if number1 > number2:
        print(number3, number1, number2)
    else:
        print(number3, number2, number1)
