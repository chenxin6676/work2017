#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading


def loop():
    print('Loopthread is %s running ... ' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread name is %s >>> %s' % (threading.current_thread().name, n))
        # time.sleep(1)
    print('Thread %s stoped ...' % threading.current_thread().name)

print('Main thread start %s running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='')
t.start()
t.join()
print('Main thread is stoped %s ... ' % threading.current_thread().name)
