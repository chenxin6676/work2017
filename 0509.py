# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """ a test module """
#
#
# __author__ = 'Chenxin'
#
# import sys
#
#
# def fn():
#     args = sys.argv
#     if len(args) == 1:
#         print('Hello one args: %s' % args[0])
#     elif len(args) == 2:
#         print('Hello two args: %s' % args[1])
#     else:
#         print('Sorry, Too many arguments!')
#
#
# if __name__ == '__main__':
#     fn()

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """ this is a test modle"""
#
# __author__ = 'Chenxin'
#
#
# import sys
#
#
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print('Your arguments is one %s' % args)
#     elif len(args) == 2:
#         print('Your arguments is two %s' % args)
#     else:
#         print('Your arguments Too many!')
#


def __privilege_1(name):
    print('Your name is 1: %s' % name)


def __privilege_2(name):
    print('Your name is 2: %s' % name)


def namep(name):
    __privilege_1(name)
    __privilege_2(name)


if __name__ == '__main__':
    # test()
    namep('Chenxin')
































