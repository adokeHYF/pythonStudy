import random

"""
装饰器的特点:
    1. 函数作为参数
    2. 要有闭包的特点
装饰器的应用: 
    1. 
    2. 
    3. 
   
"""

# 定义一个装饰器
def decorate(func):
    a = 100
    print("wrapper 外层打印测试")
    def wrapper(num):
        print('----------->11111', num)
        func(6)
        print('----------->22222')

    print("wrapper 加载完成......")
    return wrapper

@decorate
def add_shopping_cart(num):
   print(f"我是毛坯房{num}")


if __name__ == "__main__":
    add_shopping_cart(5)


