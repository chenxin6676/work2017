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
        self.__resolution = self.__width * self.__height
        return self.__resolution

dell = Screen()
dell.width = 1024
dell.height = 768
print(dell.width, dell.height, dell.resolution)
assert dell.resolution == 786432, '1024 * 768 = %d ?' % dell.resolution

