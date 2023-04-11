# 推导式
"""
列表推导式:
[表达式 for 变量 in 列表]
[out_exp_res for out_exp in input_list]
或者
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
"""
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
names = ['bob', 'alice', 'sun', 'dog', 'cat', 'diandian']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)
print('------------------------------')
"""
字典推导式:
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
"""
dic_names = {key: len(key) for key in names}
print(dic_names)
dic = {x: x ** 2 for x in range(5)}
print(dic)
print('------------------------------')
"""
集合推导式:
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""
new_set = {i ** 2 for i in range(8)}
print(new_set)
a = {x for x in 'abnbasdfqwe' if x not in 'abc'}
print(a)
print('------------------------------')
"""
元组推导式:
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
"""
a = (x for x in range(10))
print(a)  # 返回的是生成器对象
print(tuple(a))  # 将生成器对象转换为元组
