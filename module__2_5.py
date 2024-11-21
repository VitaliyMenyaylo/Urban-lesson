#Объявите функцию get_matrix и напишите в ней параметры n, m и value.
#Создайте пустой список matrix внутри функции get_matrix.
#Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
#В первом цикле добавляйте пустой список в список matrix.
#Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
#Во втором цикле пополняйте ранее добавленный пустой список значениями value.
#После всех циклов верните значение переменной matrix.
#Выведите на экран(консоль) результат работы функции get_matrix.

def get_matrix(n, m, value) :
    matrix = []
    for i in range(n) :
        matrix_list = []
        matrix.append(matrix_list)
        for j in range(m):
            matrix_list.append(value)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print("Вариант 1")
print(result1)
print(result2)
print(result3)

# Вариант 2 более простой способ двухмерной матрицы нужен только 1 цикл
def get_matrix_new(n, m, value) :
    matrix = []
    for i in range(n) :
        matrix.append([value] * m)
    return  matrix

result1 = get_matrix_new(2, 2, 10)
result2 = get_matrix_new(3, 5, 42)
result3 = get_matrix_new(4, 2, 13)
print("Вариант 2")
print(result1)
print(result2)
print(result3)
