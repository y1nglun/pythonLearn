"""元组：与列表类似，不同之处在于元组的元素不能被修改。元组写在()里，元组之间用逗号隔开"""
tuple = ('abcd', 786, 2.23, 'python', 70.2)
tinytuple = (123, 'python')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
print('------------------------------')

"""集合"""
sites = {'Google', 'Taobao', 'python', 'Facebook', 'Zhihu', 'Baidu', 'Google'}
sites2 = {'Baidu', 'Google'}  # 重复的元素会被去掉
print(sites)
print(sites - sites2)
print(sites & sites2)
print('------------------------------')
# 可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素
print('------------------------------')

"""字典:列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
   字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合"""
dict = {}
dict['one'] = "1 - python"
dict[2] = "2 - pycharm"
tinydict = {'name': 'python', 'code': 1, 'site': 'www.python.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
print(tinydict['name'])
print('------------------------------')

"""bytes：与字符串类型不同的是，bytes 类型中的元素是整数值（0 到 255 之间的整数）
   bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。在网络编程中，也经常使用 bytes 类型来传输二进制数据。
   创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。
   bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码"""

x = b"hello"
print(x)
# 由于 bytes 类型是不可变的，因此在进行修改操作时需要创建一个新的 bytes 对象
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
print(y)
print(z)
