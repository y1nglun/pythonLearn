# for循环用法
sites = ["baidu", "google", "python", "taobao"]
for site in sites:
    print(site)
print('------------------------------')

word = 'python'
for letter in word:
    print(letter)
print('------------------------------')

# range()函数
a = ['baidu', 'google', 'python', 'taobao']
for i in range(len(a)):
    print(i, a[i])
# range()函数创建列表
c = list(range(5))
print(c)
