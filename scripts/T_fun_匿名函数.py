import random
from functools import reduce

"""
匿名函数的特点:
    1. 函数作为参数
    2. 要有闭包的特点
匿名函数的应用: 
    1. map()
    2. reduce()
    3. 
    
如果装饰器是多层的，谁距离函数最近就有限使用哪个装饰器
   
"""

# map()
def map_fun():
    arr = map(lambda e: e if e % 2 == 0 else e+2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(arr))


# reduce() 对可迭代的元素进行加减乘除运算的函数
def reduce_map():
    result = reduce(lambda x,y: x*y+1, (1, 2, 3, 4))
    print(result)


if __name__ == "__main__":
    map_fun()
    reduce_map()



