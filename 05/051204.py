#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Chenxin'


class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        self.__resolution = 1024
        return self.__resolution

dell = Screen()
dell.width = 10
dell.height = 5
print(dell.width, dell.height, dell.resolution)

