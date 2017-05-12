#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chenxin'


class Student(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @property
    def score(self):
        print('diaoyong4')
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            print('diaoyong1')
            raise ValueError('Not int')
        if value < 0 or value > 100:
            print('diaoyong2')
            raise ValueError('Number must be in 0-100')
        print('diaoyong3')
        self.__score = value


s = Student('Zhangsan')
# s.set_score(59)
s.score = 60
s.score2 = 80
print(s.get_name(), s.score)
print(dir(s))
print(dir(Student))
print(type(s.score))
print(type(s.score2))
print(type(Student.score))
