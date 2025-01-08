def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print('part 1')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print('part 2')
values_list = [1, 'string', True]
values_dict = {'a': 1, 'b' : "string2", 'c' : False }
print_params(*values_list)
print_params(**values_dict)
print('part 3')
values_list_2 = [11.11, 'Строка' ]
print_params(*values_list_2, 5)
