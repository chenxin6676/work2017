__author__ = 'Chenxin'

# # 使用map高阶函数求列表各个元素的平方
# from collections import Iterator
#
#
# def func(x):
#     return x**2
# lst = [1, 2, 3, 4, 5]
# itor = map(func, lst)
# print(itor)
# print(type(itor))
# print(isinstance(itor, Iterator))
# for i in itor:
#     print(i)
#
#
# print([x for x in map(str, [1, 2, 3, 4])])
# print(list(map(str, [5, 6, 7, 8, 9, 0])))
#
# # 使用reduce计算列表和
# from functools import reduce
# lst2 = [1, 2, 3]
#
#
# def add2(x, y):
#     return x + y
#
# reds = reduce(add2, lst2)
# print(type(reds))
# print(reds)
#
# # 把列表转换成单个数字
# def fn(x, y):
#     return x*10+y
# print(reduce(fn, [1, 3, 5, 7, 9]))

# 将给出的数字字符串列表显示为串在一起的一个整数(按照列表默认顺序).
# from functools import reduce
#
#
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#
# def str2int(s):
#     return reduce(lambda x, y: x*10+y, map(char2num, s))
#
# print(str2int(['1', '3', '9']))


# 将字符串列表转换为整数显示
# from functools import reduce
#
#
# def ftl(x):
#     return x**2
# print(list(map(ftl, [1, 2, 3])))
#
#
# def add2(x, y):
#     return x+y
# print(reduce(add2, [1, 2, 3]))
#
#
# def char2num(s):
#     return {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}[s]
#
#
# def lst2int(x, y):
#     return x*10+y
# print(reduce(lst2int, list(map(char2num, ['2', '1', '3', '0', '5']))))

# 利用filter实现素数
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
#
# def _not_divisible(n):
#     return lambda x: x % n != 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

# # filter的用法
# def shaizi(n):
#     if n % 3 == 0:
#         return  n
# relt = filter(shaizi, [1, 2, 3, 5, 7, 9, 12])
# print(list(relt))

# # sorted高阶函数
# print(sorted([2, -3, 5, -9]))
# print(sorted([2, -3, 5, -9], key=abs))
# print(sorted(['Zoo', 'abc', 'Foo', 'hoo']))
# print(sorted(['Zoo', 'abc', 'Foo', 'hoo'], key=str.lower))


