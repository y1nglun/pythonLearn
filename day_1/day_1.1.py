"""
多行注释
"""
print("Hello \nworld")  # \n换行,'\'是转义符
print(r"Hello world")  # r可以让'\'转义符不发生转义
print('------------------------------')
str = '12345689'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:5:2])  # 从第2个到第5个且步长为2
print(str * 2)
print(str + 'Hello')
print('------------------------------')
abc = input()
print(abc)  # 换行输出
print(abc, end='')  # 不换行输出
print(abc)  # 换行输出
print('------------------------------')
a, b, c, d = 1, True, "hell0", 4 + 3j  # 同时赋值
print(type(a), type(b), type(c), type(d))  # 通过type()函数判断变量类型
print(isinstance(a, int))  # isinstance()函数判断变量是否为某类型
print('------------------------------')
list = ['abcd', 712, 2.22, 'hello', 11.11]
tinylist = ['abcd', 11.11]
print(list[1:])
print(list[2:5])
print(tinylist * 2)
print(list + tinylist)
"""与字符串不同的是list的元素是可以改变的"""
list[2] = 250.123
print(list)
list[2:5] = [2, 3, 4]
print(list[2:5])
print('------------------------------')
