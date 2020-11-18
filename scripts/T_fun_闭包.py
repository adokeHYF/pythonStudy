import random
# 函数
"""
闭包的应用: 
    1. 使用同级的作用域
    2. 读取其他元素的内部变量
    3. 延长作用域
    
闭包的缺点：
    1. 作用域没有那么直观
    2. 因为变量不会别垃圾机制回收所以又一定的占用问题
    
"""


def fun2(a, b):
    c = 10

    def fun2_inner():
        s = a + b + c
        print(f"相加之后的结果:{s}, a:{a}, b:{b}, c:{c}")
    return fun2_inner


# 计数器
def generate_count():
    container = [0]

    def add_one():
        container[0] = container[0] + 1
        print(f"第{container[0]}次访问")

    return add_one


if __name__ == "__main__":
    ifun_1 = fun2(10, 1)
    ifun_2 = fun2(10, 100)
    ifun_1()
    ifun_2()

    count = generate_count()
    count()
    count()
    count()
    count()
    count_1 = generate_count()
    count_1()
    count_1()
    count_1()


