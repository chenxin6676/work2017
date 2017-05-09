#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """


__author__ = 'Chenxin'

import sys


def fn():
    args = sys.argv
    if len(args) == 1:
        print('Hello one args: %s' % args[0])
    elif len(args) == 2:
        print('Hello two args: %s' % args[1])
    else:
        print('Sorry, Too many arguments!')


if __name__ == '__main__':
    fn()

    