__author__ = 'chenxin'
from types import MethodType
'''
对类的绑定方法有2种.包括通过MethodType和直接赋的方式
对实例的绑定方法只有1种可以.就是通过MethodType
'''

def set_age(self, age):
    self.age = age



class Stu(object):
    pass
# Stu.set_age=MethodType(set_age,Stu)
# Stu.set_age = set_age
A = Stu()
# B = Stu()
# A.set_age=MethodType(set_age,A)
# B.set_age=MethodType(set_age,B)
A.set_age = set_age
# B.set_age = set_age
A.set_age(10)
# B.set_age(15)
# print(A.age, B.age)
print(A.age)