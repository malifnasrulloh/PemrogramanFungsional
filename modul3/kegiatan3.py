random_list = [105, 3.1, "Hello World", 737,
               "Python", 2.7, "World", 412, 5.5, "AI"]

data_float = tuple(filter(lambda x: type(x) == float, random_list))
data_string = list(filter(lambda x: type(x) == str, random_list))
data_int = list(map(lambda x:{"ratusan":str(x)[0],"puluhan":str(x)[1],"satuan":str(x)[2]},list(filter(lambda x: type(x) == int, random_list))))
print("data_float : " , data_float)
print("data_string : " , data_string)
print("data_int : " , end="\n")
for i in data_int:
    print(i)
