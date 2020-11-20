import random

"""
装饰器的特点:
    1. 函数作为参数
    2. 要有闭包的特点
装饰器的应用: 
    1. 
    2. 
    3. 
    
如果装饰器是多层的，谁距离函数最近就有限使用哪个装饰器
   
"""


# 定义一个装饰器
def login(*args, **kwargs):
    print("加载校验")
    role = kwargs.get("role")
    def decrator(func):

        def wrapper_common(**kwargs):
            if kwargs.get("username") == "xx" and kwargs.get("password") == "123":
                func(kwargs.get("username"), kwargs.get("password"))
            else:
                print("用未登录, 请登录后再添加购物车!")


        def wrapper_mayun(**kwargs):
            print("淘宝都是马云的，白送不要钱！")

        if role == "mayun":
            return wrapper_mayun
        else:
            return wrapper_common

    print("wrapper 加载完成......")
    return decrator


@login(role="common")
def add_shopping_cart(username="", password=""):
    print(f"{username} 成功添加购物车, 密码是:{password}")


@login(role="mayun")
def mayun_add_shopping_cart(username="", password=""):
    print(f"{username} 成功添加购物车, 密码是:{password}")


if __name__ == "__main__":
    print("==========> 小明添加购物车")
    add_shopping_cart(username="小明", password=123)
    print("\n")
    print("==========> xx添加购物车")
    add_shopping_cart(username="xx", password="123")
    print("\n")
    mayun_add_shopping_cart(username="mayun", password="xxx")


