#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: chenxin
# IO的操作
# f = open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r')

print('11111111')
try:
    f = open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()
print()
print('222222222')
with open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r') as f:
    print(f.read())
print()
print('333333333')
with open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r') as file:
    line = file.readlines()
    for oneline in line:
        print(oneline.strip())

