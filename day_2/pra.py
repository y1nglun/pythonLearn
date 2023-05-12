# word = input()
# i = int(input())
# ascii_c = ord(word)
# ascii_result = ascii_c + i
# if ascii_result > ord('z'):
#     ascii_result = (ascii_result - ord('a')) % 26 + ord('a')
# print(chr(ascii_result))
# import math
#
# x = float(input())
# if x < -1:
#     y = -x + 6
# elif -1 <= x <= 2:
#     y = x ** 8
# else:
#     y = 9 * math.exp(x)
# print("%.2f" % y)

# m, n = map(int, input().split())
# count = 0
# for i in range(1, 1001):
#     if i % m != 0 or i % n != 0:
#         count += 1
# print(count)
#
# m, n, k = map(int, input().split())
#
# fib = [m, n]
# is_odd = [m % 2 == 1, n % 2 == 1]
#
# for i in range(2, k):
#     fib.append(fib[i - 1] + fib[i - 2])
#     is_odd.append(fib[i] % 2 == 1)
#
# odd_values = [fib[i] for i in range(k) if is_odd[i]]
#
# for i, val in enumerate(odd_values):
#     print("{:>8d}".format(val), end="")
#     if (i + 1) % 5 == 0:
#         print()
# if len(odd_values) % 5 != 0:
#     print()
#
# avg = sum(fib[:k]) / k
# print("{:>8.3f}".format(avg))

# with open('data.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#
# result = []
# for line in lines:
#     line = line.replace(',', '  ')
#     result.append(line)
#
# with open('result.txt', 'w', encoding='utf-8') as f:
#     f.writelines(result)


class Account():
    def __init__(self, id="1", balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, balance):
        if balance >= 1000000:
            print('请到vip办理')
        else:
            self.balance += balance
            print('成功存入%.2f' % balance + ',账户余额%.2f' % self.balance)


def main():
    user = Account("101", 1000)
    money = eval(input())
    user.deposit(money)


main()
