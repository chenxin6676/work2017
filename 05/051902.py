#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Zhangsan', '20', '98')

dic = json.dumps(s, default=lambda obj: obj.__dict__)
print('以下是json的数据格式')
print(dic)

py = json.loads(dic)
print('以下是python的数据格式')
print(py)

