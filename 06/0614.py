#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 正则表达式
import re

test = 'abc123'
if re.match(r'^a.*3$', test):
    print('ok')
else:
    print('failed')


test = '028-82272588'
m = re.match(r'^(\d{3})-(\d{3,8})$', '028-82272588')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())


m2 = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m2.group(0))


m3 = re.match(r'(.*)(@)(.*)(\.)(.*)', 'tom.chen@tom.gov.cn')
print(m3.groups())
print(m3.group(1))



# test

