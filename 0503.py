

fs = map(lambda x: x * x, [1, 2, 3, 4])
print(list(fs))

fa = lambda x: x * 2
print(fa(11))


def build(x, y):
    return lambda: x + y

print(build(10, 20)())

fb = build(20, 30)
print(fb())

# 比较以下2个的不同之处,注意计算结果的差异(闭包:一个是绑定了参数的函数,一个是未绑定参数的函数)
squares = []
for x in range(5):
    squares.append(lambda n=x: n**2)
print([x() for x in squares])

squares = []
for x in range(5):
    squares.append(lambda: x**2)
print([x() for x in squares])
