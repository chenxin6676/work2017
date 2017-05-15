#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chenxin'


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().a1.a2.b3)