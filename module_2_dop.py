import random # Для автоматизации подключу модуль рандом
ent_number = random.randint(3, 20) #случ число из диапазона

#ent_number = input("Введите число от 3 до 20 ") # ручной ввод

matrix_par = []
for i in  range(1,20) :
    for j in range(i+1, 21) :
        if ent_number%(i+j)==0 :
            matrix_par.append([i,j])
            continue

print(ent_number)
print(matrix_par)

