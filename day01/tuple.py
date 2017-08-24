# Auther hr.Sun
# 有序列表叫元组：
# tuple和list非常类似，但是tuple一旦初始化就不能修改
# 它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 因为tuple不可变，所以代码更安全
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])

len(classmates)

# 因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
# 表示数学公式中的小括号
t = (1)
print(t)
# 表示tuple，只有1个元素的tuple定义时必须加一个逗号，来消除歧义
t = (1,)
print(t)

# “可变的”tuple
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
