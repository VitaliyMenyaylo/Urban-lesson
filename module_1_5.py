
elem_0 = "string"
elem_1 = 1
elem_2 = True
elem_3 = 1.5
immutable_var = elem_0, elem_1, elem_2, elem_3
print(immutable_var)
print(type(immutable_var))
elem_4 = "Modified"
print(immutable_var[0])
#immutable_var[0] = elem_4 # не сработает, т.к. кортеж не изменяем, не сработает даже при переопределении переменной
elem_0 = elem_4
print(elem_0)
print(immutable_var[0] == elem_0) # несмотря на одинаковое имя объекта, кортеж помнит значение при определении (т.е. ссылку на первый объект elem_0)
immutable_var_0 = elem_4
immutable_var = (immutable_var) + (elem_4,) # присоединим к первому кортежу второй состоящий из одного элемента
print(immutable_var)
elem_0 = "string"
mutable_list = [elem_0, elem_1, elem_2, elem_3] #Получим список.
mutable_list[0]=elem_4
print(mutable_list) #Элемент списка изменен
mutable_list[0]=elem_0
mutable_list = mutable_list + [elem_4]
print(mutable_list) #К списку добавлен еще один элемент


