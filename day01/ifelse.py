# Auther hr.Sun
# 条件判断
# 用if语句实现
# 注意不要少写了冒号:
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

# input()读取用户的输入
birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')

# 输入1982，结果报错
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unorderable types: str() > int()

# 因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。
# int() 把str转换成整数
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')