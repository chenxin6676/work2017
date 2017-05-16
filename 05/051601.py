#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chenxin'


from enum import Enum,unique


Month = Enum('Month', 'A, B, C, D, E, F, G')
for name, member in Month.__members__.items():
    print(name, member, member.value)


class Weekday(Enum):
    A = 1
    B = 2
    C = 3

for name, member in Weekday.__members__.items():
    print(name, member, member.value)