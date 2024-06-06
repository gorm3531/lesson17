def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(2)
print_params('help', 7)
print_params(2.1, False, 'try')
print_params(b = 25)
print_params(c = [1,2,3]) #1
values_list = ['What', 3531, False]
values_dict = {'a': 8, 'b': 'хех', 'c': False}
print_params(*values_list)
print_params(**values_dict) #2
values_list_2 = [397, 'win']
print_params(*values_list_2, 42)






