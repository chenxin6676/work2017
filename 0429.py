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


