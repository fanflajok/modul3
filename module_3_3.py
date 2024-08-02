def print_params(a = 1, b = "строка", c = True):
    print(a,b,c)
print_params()
print_params(3, c = [1,2,3])
print_params(1000, b=25)
print_params(c = 3>4)
values_list = 100, "Dynamo", [3,2,1]
values_dict = {"a" : "Victor", "b" : "6==6", "c" : "[10,100,100]"}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = "Марио", [6,4]
print(values_list_2)
print_params(*values_list_2, 42)
