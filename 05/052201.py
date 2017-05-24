#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fn(n):
    if n == 1:
        return n
    elif n > 1:
        return n * fn(n - 1)


print(fn(5))


class Student(object):
    def __init__(self, name, score):
        self._name = name
        self.__score = score

    def prin(self):
        print(self._name)

    def pris(self):
        print(self.__score)


s = Student('zhangsan', 90)
s.prin()
print(s._name)
print(s.__score)
# s.pris()

