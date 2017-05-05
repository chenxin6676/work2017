# 以下为回顾模块以前的讲解内容


# def sum2(*nums):
#     s = 0
#     for i in nums:
#         s = s + i
#     return s
# l = [1, 2, 3, 4]
# print(sum2(*l))
#
#
# a = 'this is a test'
# for i in a.split(' '):
#     print(i)
#


# #递归 n * (n-1) * (n-2) * ... * 1 = recu(n-1)*n
# s = 1
#
#
# def recu(m):
#     if m > 1:
#         s = recu(m-1) * m
#         return s
#     else:
#         s = s * m
#         return s
#
# print(recu(5))

# # 求阶乘
# def recu(m):
#     if m == 1:
#         return 1
#     else:
#         return recu(m-1)*m
# print(recu(5))


# # 斐波那契额数列
# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(5))

# 汉诺塔
def hannuota(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
#     elif n == 2:
#         print(a, '-->', b)
#         print(a, '-->', c)
#         print(b, '-->', c)
    else:
        hannuota(n-1, a, c, b)
        hannuota(1, a, b, c)
        hannuota(n-1, b, a, c)
hannuota(3, 'A', 'B', 'C')
