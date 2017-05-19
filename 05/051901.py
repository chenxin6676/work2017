#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = os.listdir('.')
for x in os.walk(os.path.realpath('.')):
    filelist = x[2]
    for onefile in filelist:
        if os.path.splitext(onefile)[1] == '.py':
            print(onefile, os.path.realpath(onefile))








