#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: chenxin
# IO的操作
# f = open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r')


# try:
#     f = open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# with open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r') as f:
#     print(f.read())
# with open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r') as file:
#     line = file.readlines()
#     for oneline in line:
#         print(oneline.strip())
# with open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'a') as writefile:
#    writefile.write('6 line\n')

import time

with open('/Users/chenxin/gitsvn/localwork/05/0518.txt', 'r+') as readfile:
    # eveline = readfile.readlines()
    # for line in eveline:
    #     print(line.strip())
    readfile.write('Hello world4\n')
    # time.sleep(2)
    for i in readfile.readlines():
        print(i.strip())
