# 函数
"""
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""
"""
    def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

    def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
"""


# 函数传参

# 函数传参默认值
def people(name, gender="boy", list=None):
    if list is None:
        list = ["address", "language"]
    print(name, gender, list)


people("zhangSan")

# 函数的可变参数
p1 = [1, 2, 3]


def worker(*params):
    for i in params: print(i)

    print(params)


worker(*p1)
#  worker(*[1, 2, 3])  //[1, 2, 3]

# 函数的关键词函数


def boss(name, **kwargs):
    print(name, kwargs)


boss("lim", age=12, gender="boy")
