#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Chenxin'


class Student(object):
    # __slots__ = ('name', 'age')
    pass

def register(name):
    print(name)



s = Student()
s.name = 'chenxin'
s.age = 20
print(s.name, s.age)
s.score = 100
print(s.score)





# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# __author__ = 'Chenxin'
# '''练习setattr(),getattr()的用法'''
#
# class Student(object):
#     student_number = 0
#
#     def __init__(self, name):
#         self.name = name
#
#
# def register(name, **kwargs):
#     a = Student(name)
#     for k, v in kwargs.items():
#         setattr(a, k, v)
#     Student.student_number += 1
#     return a
#
# bob = register(Student('Bob'), score=90)
# ah = register(Student('Ah'), age=8)
# print(getattr(bob, 'score'))
# print(getattr(ah, 'age'))
# print(Student.student_number)



