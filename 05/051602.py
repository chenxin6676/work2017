#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chenxin'

# 错误调试

def fn(s):
    try:
        print('Try ...')
        # return 10/s    # 这里有了return,会造成后面的else语句无法执行(pycharm也会提示else无论给什么条件都不会执行的提示信息)
        r = 10/s
        print(r)
    except ValueError as e:
        print('ValueError --- print')
        print(e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError --- print')
        print(e)
    except TypeError as e:
        print('TypeError --- print')
        print(e)
    else:
        print('No error')
    finally:
        print('Finally...')


print(fn('Hello'))
print('-------------')
print(fn(20))
print('--- END ---')


try:
    print('try...')
    r = 10/int('2')
    print('result:', r)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print('No error')
finally:
    print('finally')
print('EMD')
