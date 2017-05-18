#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: chenxin
# IO的操作
# f = open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r')

try:
    f = open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()


with open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r') as f:
    print(f.read())

