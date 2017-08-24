# Auther hr.Sun
# 循环
# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来

classmates = ['Lily','Luce','Tome','Babel']
for classmate in classmates:
    print(classmate)

# Python提供一个range()函数，可以生成一个整数序列 range(5)生成的序列是从0开始小于5的整数
# list()函数可以转换为list
print(list(range(5)))  # [0, 1, 2, 3, 4]

# range(101)就可以生成0-100的整数序列
# 0+1+2+3+4+5+...+100 = ?   高斯函数
sum = 0
for x in list(range(101)):
    sum = sum + x
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)