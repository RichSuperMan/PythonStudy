# Auther hr.Sun
#list list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
#用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(classmates[0])
print(classmates[1])
print(classmates[2])
#用-1做索引，直接获取最后一个元素，-2可以获取倒数第2个、-3倒数第3个
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
#添加记录，有序添加
classmates.append('Adam')
print(classmates)
#指定位置插入记录
classmates.insert(1,'Lily')
print(classmates)
#要删除list末尾的元素，用pop()方法
classmates.pop()
#删除指定位置的记录
classmates.pop(2)
print(classmates)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[0] = 'Sarah'
print(classmates)
#用len()函数可以获得list元素的个数
print(len(classmates))
#list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
#list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
# 要注意s只有4个元素，其中s[2]又是一个list
len(s)