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


from enum import Enum

Month = Enum('Month2', 'Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec')

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

