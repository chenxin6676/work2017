#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chenxin'
'''
这里介绍的是实例绑定变量或绑定方法中,__slots__的用法
'''

class Student(object):
    __slots__ = ('name', 'age', 'register')
    pass


s = Student()
s.name = 'Chenxin2'
s.age = 30
print(s.name, s.age)


def register(self, name):
    self.name = name
    print(self.name)


from types import MethodType


s.register = MethodType(register, s)

s.register(20)