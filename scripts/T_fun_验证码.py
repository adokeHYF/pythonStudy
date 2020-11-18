import random
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


def generate_check_code(n):
    code_str = "zhanghZhHOIYIOHUUGTOLHUILKJY1563839263829032"
    code = ""
    for i in range(n):
        code += code_str[random.randint(0, len(code_str))]

    return code


def login(username, password):
    for i in range(3):
        if username == "xx" and password == "123":
            code = generate_check_code(4)
            code_input = input(f"请输入验证码: {code}: ")
            if code_input.lower() == code.lower():
                print("登陆成功")
            else:
                print("登陆失败")
            break
        else:
            print("登陆失败")
            username = input("输入用户名: ")
            password = input("输入密码: ")
    else:
        print("账户锁定")


if __name__ == "__main__":
    username = input("输入用户名: ")
    password = input("输入密码: ")
    login(username, password)
