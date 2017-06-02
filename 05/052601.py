#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('This is my pid: %s' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child, pid %s, and my parent is %s' % (os.getpid(), os.getppid()))
else:
    print('I am paranet, pid %s, and child pid is %s' % (os.getpid(), pid))
