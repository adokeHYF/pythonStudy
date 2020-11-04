# 元组
# 元组类似列表
# 1. 定义符号()
# 2. 元组中的内容不可修改
# 3. 关键词： tuple
# 系统函数
"""
max()
min()
sum()
len()
sorted() 返回一个list
tuple() 元组类型强制转换
index()
count()

"""

t_str = ("lili", "haha",)

t_num = (1, 2, 3, 4, 5, 6,)

# 增: 没有方法

# 删: 没有方法

# 改: 没有方法

# 查: 切片的方式

# <tuple>.index(var) 这个tuple 中 var 第一次出现的索引值

# <tuple>.count(var) 这个tuple 中 var 的 个数

print(max(t_num))

# 拆包
name1, name2 = t_str
print(f"name1:{name1}, name2:{name2}")

# 变量与拆包的元素个数不一致
num1, *num_list, num6 = t_num
print(f"num1:{num1}, num list:{num_list}, num6:{num6}")


