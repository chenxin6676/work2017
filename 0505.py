# 以下为回顾模块以前的讲解内容


def sum2(*nums):
    s = 0
    for i in nums:
        s = s + i
    return s
l = [1, 2, 3, 4]
print(sum2(*l))

