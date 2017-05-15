#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chenxin'


class Student(object):
    def __init__(self):
        self.name = 'Michel'

    def __getattr__(self, item):
        if item == 'score':
            return 65
        elif item == 'age':
            return lambda: 15
        else:
            return 'No the attr(item): %s' % item

s = Student()
print(s.name)
print(s.score)
print(s.age())
print(s.xingbie)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().a1.a2a.a3.a4)


