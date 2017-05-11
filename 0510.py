#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Chenxin'


# class Student(object):
#     def __init__(self, name, score, sex='Male'):
#         self.__name = name
#         self.__score = score
#         self.__sex = sex
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def get_sex(self):
#         return self.__sex
#
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('Bad value')
#
#     def set_sex(self, sex):
#         self.__sex = sex
#
# zhangsan = Student('Zhangsan', 90, 'Female')
# print(zhangsan.get_score())
# zhangsan.set_score(10)
# print(zhangsan.get_score())
# print(zhangsan.get_sex())
# zhangsan.set_sex('Nanren')
# print(zhangsan.get_sex())


class Animal(object):
    def run(self):
        print('Animal is running!')


class Dog(Animal):
    def run(self):
        print('Dog is running!')


class Cat(Animal):
    pass


def run_twice(animal):  # 这里为什么是小写的animal,而不是大些的呢?因为大些的会和类Animal冲突.
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


class Tort(Animal):
    def run(self):
        print('Tort is running slowly...')

run_twice(Tort())


class Car(object):
    def run(self):
        print('The Car is running')

run_twice(Car())



