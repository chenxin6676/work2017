__author__ = 'chenxin'


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():  #这里的定义函数没有带参数,可以跟下面定义的f函数对比
#             return i*i
# #        fs.append(f)
#         fs.append(f())
#     return fs
# print(count())
# # for j in count():
# #     print(j())


def count():
    fs = []
    for i in range(1, 4):
        def f(i):  # 这行的i,就和上面一行的i没有任何关系了
            return i*i
        fs.append(f)
    return fs
print(count())
f1, f2, f3 = count()
print(f1(5))
print(f2(9))
print(f3(1))