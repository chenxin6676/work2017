__author__ = 'chenxin'


def double(n):
    return n*2
result = map(double, [1, 2, 3, 4])
print([x for x in result])
# print(list(result))  # ->[]
# print([x for x in result])  # ->[]


from functools import reduce


def add(x, y):
    return x+y
result2 = reduce(add, [1, 2, 3, 4, 5])
# print(isinstance(result2, int))
# print(type(result2))


def fn(x, y):
    return x*10+y
result3 = reduce(fn, [1, 2, 3, 4])
print(result3)
print('##################')

L = ['adam', 'LISA', 'barT']


def tran(s):
    return s.capitalize()
print(list(map(tran, [x for x in L])))

print('##################')


def prod(x, y):
    return x*y
print(reduce(prod, [1, 2, 3, 4]))

print('########以下是filter函数用法##########')


def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))


def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', None, 'C', ' '])))




