#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单元测试


class A(object):    # A must be new-style class
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):     # A --> C
    def __init__(self):
        print('enter B')
        super(B, self).__init__()   # 这里就相当于A.__init__(self) 目的是为了当B的父类由A变成C的时候,B的代码无需更改(当代码量很大时,就非常方便了).
        print('leave B')

test = B()
