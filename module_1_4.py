#Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
#Вывести количество символов введённого текста
#3. Работа с методами строк:
#Используя методы строк, выполните следующие действия:
#Выведите строку my_string в верхнем регистре.
#Выведите строку my_string в нижнем регистре.
#Измените строку my_string, удалив все пробелы.
#Выведите первый символ строки my_string.
#Выведите последний символ строки my_string

my_string = input("Введите строку, для разбора: ")
#my_string ="From fairest creatures we desire increase,"
print(my_string)
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(" ",""))
print(my_string[0])
print(my_string[-1])
