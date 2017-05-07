# 以下为回顾模块以前的讲解内容

# # 列表作为参数的调用,可以直接用*加上列表名字
# def sum2(*nums):
#     s = 0
#     for i in nums:
#         s = s + i
#     return s
# l = [1, 2, 3, 4]
# print(sum2(*l))


# #递归
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

# # 汉诺塔
# def hannuota(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
# #     elif n == 2:
# #         print(a, '-->', b)
# #         print(a, '-->', c)
# #         print(b, '-->', c)
#     else:
#         hannuota(n-1, a, c, b)
#         hannuota(1, a, b, c)
#         hannuota(n-1, b, a, c)
# hannuota(3, 'A', 'B', 'C')

# # 已知：数列1,1,2,4,7,13,24,44,...求数列的第 n项.(前面3个数字相加)
# def func(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n == 3:
#         return 2
#     else:
#         return func(n-1) + func(n-2) + func(n-3)
# print(func(3))

# # 列出奇数
# def func(n):
#     if n == 1:
#         return 1
#     else:
#         return func(n-1)+2
# print(func(5))

# # 迭代;以及另一种数据类型-枚举
# L = ['a', 'b', 'c']
# for index, value in enumerate(L, 2):
#     print(index, value)
# print(L)
# print(type(enumerate(L)))
# print([x for x in enumerate(L)])


# # 列表生成式
# L1 = ['A', 'B', 'C']
# L2 = ['X', 'Y', 'Z']
# print([x+y for x in L1 for y in L2])

# 递归列表最大值
def maxlist(L, n):
    if n == 0:
        return L[0]
    else:
        if L[n] > maxlist(L[n-1], n-1):
            return L[n]
        else:
            return maxlist(L[n-1], n-1)
print(maxlist([1, 2], 1))



