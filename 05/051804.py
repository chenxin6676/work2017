#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 讲解StringIO和BytesIO,涉及到seek()和tell().
from io import StringIO, BytesIO

f = StringIO('T\nShazi\nERhuo\nGoodbye')
f.write('Hello')
print(f.tell())
f.seek(0)
# f.write('   ')
# f.write('World!')
# # print(f.getvalue())
# print('!!!')
# # print(f.read())
# for i in f.readlines():
#     print(i.strip())
print(f.tell())
print(f.getvalue())
print('###')
print(f.tell())
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
print(f.tell())

f = BytesIO('中文'.encode('utf-8'))
print(f.getvalue())
