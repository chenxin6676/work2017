__author__ = 'chenxin'


print(sorted([-1, -2, 3, 2, 9, 7]))
print(sorted([-1, -2, 3, 2, 9, 7], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]
print(sorted(L, key=by_name))


def by_score(t):
    return t[-1]
print(sorted(L, key=by_score, reverse=True))

print(sorted(L, key=lambda x: x[0]))
print(sorted(L, key=lambda x: x[1], reverse=True))