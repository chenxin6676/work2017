#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Fooerr(ValueError):
    pass

def fn(s):
    n = int(s)
    if n == 0:
        raise Fooerr('invalid value: %s' % s)
    return 10/s

fn(0)