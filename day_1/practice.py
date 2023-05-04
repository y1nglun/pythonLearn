# import random
#
# m, n = map(int, input().split(','))
#
# random.seed(50)
# matrix = [[random.randint(0, 100) for j in range(n)] for i in range(m)]
#
# for row in matrix:
#     row_sum = sum(row)
#     row_str = ' '.join(map(str, row))
#     print(row_str, 'sum={}'.format(row_sum))


# m, n = map(int, input().split(','))
# matrix = [[i] * n for i in range(1, m + 1)]
# for row in matrix:
#     print(*row)


# animals = []
# while True:
#     input_str = input()
#     if input_str == '-1':
#         break
#     animal, weight = input_str.split()
#     animals.append([animal, weight])
#
#
# def convert_weight(weight_str):
#     # 获取重量数值和单位
#     weight = float(weight_str[:-2])  # 去掉最后两个字符并转换为数值
#     unit = weight_str[-1:]
#     # 根据重量单位进行转换
#     if unit == "g":
#         return weight
#     elif unit == "t":
#         return weight * 1000
#     else:
#         raise ValueError("Unexpected unit: " + unit)
#
#
# animals_sorted = sorted(animals, key=lambda x: convert_weight(x[1]))
# print(animals_sorted)

# scores = input().split()
# if not scores:
#     print(0)
# else:
#     scores = [int(score) for score in scores if score != '-1']
#     if not scores:
#         print(0)
#     else:
#         avg_score = sum(scores) / len(scores)
#         count = sum(1 for score in scores if score > avg_score)
#         print(count)

# list = []
# for i in range(10):
#     n = int(input())
#     list.append(n)
# list.reverse()
# print(*list)


