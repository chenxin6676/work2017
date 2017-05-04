
#
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


# 带text参数的装饰器log
import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('Log is:', text, args, kwargs, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('excute test')
def foo1(x):
    return 'TEST' + x

print(foo1('chenxin'))
print(foo1.__name__)

