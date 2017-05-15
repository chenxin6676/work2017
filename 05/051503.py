#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chenxin'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('Your name is : %s' % self.name)


s = Student('Michle')
s()

# 以下是枚举类的例子

from enum import Enum

Month = Enum('Month', 'A, B, C, D')
for name, member in Month.__members__.items():
    print(name, member, member.value)


from enum import Enum, unique


@unique
class Weekday(Enum):
    M = 1
    T = 2
    S = 3

for name, member in Weekday.__members__.items():
    print(name, member, member.value)


for i in Weekday.__members__.items():
    print(i)
    print(type(i))




