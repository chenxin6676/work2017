__author__ = 'chenxin'


def lazy_sum(*args):
    def sum2():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    # return sum2()
    return sum2
f = lazy_sum(1, 2, 3, 4, 5)
print(f)
print(f())
print('###########')
f1 = lazy_sum(1, 2, 3)
f2 = lazy_sum(1, 2, 3)
print(f1 == f2)
print(f1())
print(f2())
print('!!!!!!!!!!!!')


def count():
    fs = []
    for i in range(1, 4):
        def f_2():
            return i*i
        fs.append(f_2)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())