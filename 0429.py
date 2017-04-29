__author__ = 'chenxin'


def double(n):
    return n*2
result = map(double, [1, 2, 3, 4])
print([x for x in result])
print(list(result))  # ->[]
print([x for x in result])  # ->[]
