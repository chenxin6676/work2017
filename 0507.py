__author__ = 'Chenxin'

# 使用map高阶函数求列表各个元素的平方
from collections import Iterator


def func(x):
    return x**2
lst = [1, 2, 3, 4, 5]
itor = map(func, lst)
print(type(itor))
print(isinstance(itor, Iterator))
for i in itor:
    print(i)


print([x for x in map(str, [1, 2, 3, 4])])
print(list(map(str, [5, 6, 7, 8, 9, 0])))

# 使用reduce计算列表和
from functools import reduce
lst2 = [1, 2, 3]


def add2(x, y):
    return x + y

reds = reduce(add2, lst2)
print(type(reds))
print(reds)

# 把列表转换成单个数字
def fn(x, y):
    return x*10+y
print(reduce(fn, [1, 3, 5, 7, 9]))