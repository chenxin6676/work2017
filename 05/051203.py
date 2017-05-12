#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chenxin'


class Student(object):
    @property
    def score(self):
        print('one')
        return self.__score

    @score.setter
    def score(self, value):
        print('two')
        self.__score = value



lisi = Student()
print(dir(Student))
print(dir(lisi))
print('###########')
lisi.score = 60

