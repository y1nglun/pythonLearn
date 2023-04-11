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
