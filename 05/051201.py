#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chenxin'


class Student(object):
    __slots__ = ('name')

    def __init__(self, name):
        self.name = name


zhangsan = Student('Zhangsan')
print(zhangsan.name)
