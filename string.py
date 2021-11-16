info_str = "hellopython"
info_str2 = '这是字符串外部的内容"这是字符串中的引号内容"'
info_str3 = " \t\n\r"
info_str4 = "13423"
info_str5 = "\u00b3"
info_str6 = "一千一百"

print(info_str)
print(info_str2)
print(info_str[6])

for s in info_str2:
    print(s)

print(len(info_str2))
print(len(info_str))
print(info_str.count("he"))
print(info_str.index("py"))
print("------")

print(info_str.isspace())
print(info_str2.isalpha())
print(info_str.isalpha())
print(info_str.isalnum())
print(info_str.isascii())
print("------")

print(info_str4.isdigit())
print(info_str4.isdecimal())
print(info_str4.isnumeric())
print(info_str5)
print(info_str5.isdecimal())
print(info_str6.isnumeric()) # 英文及中文数字都可以判断
print("------")

print(info_str3.isspace())


print(info_str.startswith("hea"))
print(info_str.find("lo"))

info_str_new = info_str.replace("python","swift")
print(info_str)
print(info_str_new)

# info_str.ljust()
# info_str.rjust()
# info_str.center()


poem = ["登鹳雀楼","王之涣","白日依山尽","黄河入海流","欲穷千里目","更上一层楼"]
for s in poem:
    print("|%s|" % s.center(16, "　"))