
#Входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# (Используем немного больше команд чем прошли в модуле)
#Преобразуем множество в список и отсортируем
new_student=list(students)
new_student.sort()
#-----------------------------------------------------
new_grades = [(round(sum(n)/len(n),2)) for n in grades] #получим новый список перебором элементов с записью вместо элемента верхнего списка -> среднего значение вложенного списка (с точностью 2 знака)
Journal = dict(zip(new_student, new_grades)) #Создадим словарь объединяя два списка
print(Journal)#Выведем полученный словарь содержащий ключ имя ученика и средний балл

#Вариант 2

# Получаем список средних значений
average_list = list(map(lambda sublist: round(sum(sublist) / len(sublist),2), grades))
NewJournal = dict(zip(new_student, average_list)) #Создадим словарь объединяя два списка
print(NewJournal)
