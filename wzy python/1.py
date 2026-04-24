greet = "您好"
greet_chinese ="您好"
greet_english = "hello"
greet = greet_english
print(greet + "张三")
print(greet + "李四")
print(greet + "艾君")
print(greet_chinese + "王五")
#算术
a = -1
b = -2
c = 3
print((-b + (b ** 2 - 4 * a * c)**(1/2)) / (2 * a))
print((-b - (b ** 2 - 4 * a * c)**(1/2)) / (2 * a))

import math 
a = 1
b = 9
c = 20
dalta = b ** 2 - 4 * a * c
print((-b + math.sqrt(dalta)) / (2 * a))
print((-b - math.sqrt(dalta)) / (2 * a))

a = -1
b = -2
c = 3
this = b ** 2 - 4 * a * c
print((-b + (this)**(1/2)) / (2 * a))
print((-b - (this)**(1/2)) / (2 * a))
# 字符串长度
s = "hello world"
print(len(s))
#通过索引获取单个字符串
print(s[0])
print(s[len(s) - 1])

#布尔类型
b1 = True
b2 = False

#空值类型
n = None

#type函数
print(type(s))
print(type(b1))
print(type(n))
print(type(2.3))

shopping_list = []
shopping_list.append('键盘')
shopping_list.append("键帽")
shopping_list.remove("键帽")
shopping_list.append("音响")
shopping_list.append("电竞椅")
shopping_list[1] = "硬盘"
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])

price = [700,800,900]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
print(max_price)
print(min_price)
print(sorted_price)

slang_dict = {"觉醒年代":"觉醒年代是"
              "YYDS":"YYDS是永远的神"}
slang_dict = ["双减"] = "双减是"

query = input("请输入：")
if query in  slang_dict:
    print("你查询的" + query + "含义如下")
    print(slang_dict[query])
else:
    print("您查询的为：")
    print("当前辞典条数为：" + str(len(slang_dict)) + "条。")