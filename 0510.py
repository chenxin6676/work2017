#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chenxin'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def print_grade(self):
        if self.score < 60:
            print(self.name, ':bu ji ge')
        else:
            print(self.name, ':very good')

zhangsan = Student('Zhangsan', 30)
lisi = Student('Lisi', 69)

zhangsan.print_score()
lisi.print_score()
zhangsan.print_grade()
lisi.print_grade()

