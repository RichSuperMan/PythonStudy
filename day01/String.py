# Auther hr.Sun
# 字符串操作
# str是不变对象，而list是可变对象
# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

# 获取字符串长度
len = len('ABC')
print(len)
#字符串格式化
#%运算符就是用来格式化字符串的。
# 在字符串内部，%s表示用字符串替换，
# %d表示用整数替换，
# 有几个%?占位符，
# 后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
a = 'Hello, %s' % 'world'
print(a)
b = 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print(b)

a = ['a','c','b','d']
a.sort()
print(a)  # ['a', 'b', 'c', 'd']

str = 'ACB'
str.replace('A','a')
print(str)  # 'ACB'
str1 = str.replace('A','a')
print(str1)     # 'aCB'