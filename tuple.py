info_tuple = ("zhangsan", 12, 2.2)

print(info_tuple[0])

for i in info_tuple:
    print(i)

info_list = [1, 3, 4, 6, 8]

print("%s 年龄是 %d 身高是 %.2f" % ("小明", 18, 1.75))
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)

type(info_str)
type(info_tuple)

info_dictionary = {"name": "张三",
                   "age": 14,
                   "gender": True,
                   "height": 175,
                   "weight": 65.5}

print(info_dictionary)
print(info_dictionary["name"])
print(info_dictionary["height"])

info_dictionary["height"] = 169
info_dictionary["hoby"] = "play game"
info_dictionary["birthday"] = "01-01"

print(info_dictionary["height"])
print(info_dictionary)

info_dictionary.pop("hoby")
print(info_dictionary)

print(len(info_dictionary))

temp_dictionary = {"color": "blue"}
info_dictionary.update(temp_dictionary)
print(info_dictionary)

print(info_dictionary.items())
print(info_dictionary.keys())
print(info_dictionary.values())

for k in info_dictionary:
    print(k)
    print("%s-%s" % (k, info_dictionary[k]))

dict_list = [{"name": "zs", "age": 16},
             {"name": "ls", "age": 18}]

for d in dict_list:
    print(d)

info_dictionary.clear()
print(info_dictionary)


