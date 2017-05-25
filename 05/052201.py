#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 属性函数装饰器的使用@property


class Stu(object):
    # def __init__(self, name, score):
    #     self.name = name
    #     self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score is not int!')
        if value < 0 or value > 100:
            raise ValueError('score shuld between 0-100')
        self._score = value

    @score.deleter
    def score(self):
        print('This is a test!')


# s = Stu('Zhangsan', 99)
# print(s.name, s.score)
s = Stu()
s.name = 'Zhangsan'
s.score = 100
print(s.name, s.score)

