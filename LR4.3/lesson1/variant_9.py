""" 9.	Дана последовательность символов S1, ..., Sn.
Преобразовать последователь-ность S1, ..., Sn, заменив в ней все восклицательные знаки точками. """

text = ['Hello Wrld! What are you ?', 'asd!sd!/', 'sdsaviwev']
text_new = []

for word in text:
    text_new.append(word.replace('!', '.'))  # в новый массив вставляем переделанные элементы
text = text_new  # присваиваем новые данные массива

print(text)