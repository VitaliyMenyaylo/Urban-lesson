my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_list = len(my_list)
print (index_list)
shet = 0
while shet <  index_list :
    if my_list[shet] > 0 :
        print(my_list[shet])
        shet = shet + 1
    elif my_list[shet] < 0 :
        break
    else :
        shet = shet + 1
        continue



