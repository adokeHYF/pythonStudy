import random
from functools import reduce
import functools

# 不带参数的装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 带参数的装饰器
def log(text):
    def decrator(func):
        def wrapper(*args, **kwargs):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decrator


# @log
@log("vimom")
def now():
    print('2015-3-25')


if __name__ == "__main__":
    now()
