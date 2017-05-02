__author__ = 'chenxin'


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
#        fs.append(f)
        fs.append(f())
    return fs
print(count())
# for j in count():
#     print(j())


