#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chenxin'


class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Your name is %s, Hello!' % self.__name
    __repr__ = __str__



s = Student('Mechile')
print(s)
Student('Zhangsan')