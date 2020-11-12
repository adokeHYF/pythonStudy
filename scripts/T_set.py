"""
关键词: set
作用 去重
内置函数：
    增加： add(), update()
    删除： remove(), discard() pop() clear()
    运算： difference()->差集 symmetric_difference() 对称差集-> intersection() -> 交集 union() ->并集

"""

list_1 = [4, 5, 8, 9, 1, 2, 0]
list_2 = [7, 2, 4, 8, 9, 1]
s1 = set(list_1)
s2 = set(list_2)

# 对称差集(两个列表中不一样的元素)
print(f"对称差集: {(s1 | s2) - (s1 & s2)}")

# 两个列表中不一样的元素
print(f"两个列表中不一样的元素: {s1 ^ s2}")

# 差集
print(f"差集: {s1 - s2}")

# 交集
print(f"交集: {s1 & s2}")

# 并集
print(f"并集: {s1 | s2}")

"""
求s1 和 s2 的对称差集并赋值s1, 下面同理
s1.symmetric_difference_update(s2)

交集并赋值
s1.intersection_update(s2)

并集并赋值
s1.union()
"""

s3 = set([1, 2, 3])
print(f"s3: {id(s3), s3}")

s3.pop()
print(f"s3: {id(s3), s3}")


