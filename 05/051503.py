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
