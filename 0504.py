print('以下是装饰器内容')

# def func(x, y):
#     return x + y
# lit = [1, 2]
#
# print(func(*lit))
#
# dct = {'x': 1, 'y': 2}
# print(func(**dct))


# def loger(func):
#     def inner(*args, **kwargs):
#         print('Log file is', args, kwargs)
#         return func(*args, **kwargs)
#     return inner
#
#
# @loger
# def foo1(x, y=1):
#     return x + y
# print(foo1(2, 3))
#
#
# @loger
# def foo2():
#     return 2
# print(foo2())
#

# def loger(func):
#     def inner(*args, **kwargs):
#         print('Log is:', args, kwargs)
#         return func(*args, **kwargs)
#     return inner
#
#
# @loger
# def foo1(x, y=0):
#     return x + y
# print(foo1(1, 2))
#
#
# @loger
# def foo2():
#     return 1 + 5
# print(foo2())
#

# def log(func):
#     def wrapper(*args, **kwargs):
#         print('Call name is:', func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @log
# def now():
#     print('2015')
# now()
# print(now.__name__)


# # 不带参数的装饰器log
# import functools
#
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Log is:', args, kwargs, func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @log
# def foo1(x, y):
#     return 2 + x + y
# print(foo1(10, 20))
# print(foo1.__name__)
#
#
# # 带text参数的装饰器log
# import functools
#
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print('Log is:', text, args, kwargs, func.__name__)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @log('excute test')
# def foo2(x):
#     return 'TEST' + x
#
# print(foo2('chenxin'))
# print(foo2.__name__)
#
#


import functools


def call(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print('begin call')
                print(func(*args, **kwargs), text)
                print('end call')
                # return func(*args, **kwargs)
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kwargs):
            print('begin call')
            print(text(*args, **kwargs))
            print('end call')
        return wrapper


@call('thisistext')
def foo1(x):
    # print('OK')
    return x
foo1(123)


@call
def foo2():
    return 2
foo2()


print('以下为偏函数')
# 以下为偏函数内容

import functools


int2 = functools.partial(int, base=2)
print(int2('100'))
print(int2('101', base=10))
max2 = functools.partial(max, 10)
print(max2(4, 6, 9, 11))


def mod(m, n):
    return m % n
print(mod(10, 3))
mod2 = functools.partial(mod, n=4)
print(mod2(8))
print(mod2(10))