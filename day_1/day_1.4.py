"""隐性类型转换"""
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))
print('------------------------------')

"""显性类型转换"""
num1 = 123
num2 = "456"

print(type(num1))
print(type(num2))
num2 = int(num2)
num3 = num1 + num2
print(type(num2))
print(num3)
