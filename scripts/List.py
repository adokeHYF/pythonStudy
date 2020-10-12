import random

names = ["jack", "tom", "zhangsan"]
for name in names:
    if name == "tom":
        print("名称存在")
        break
    pass

print(names[1:])

# append() 末尾追加
names.append("lisi")

# insert() 指定位置追加
names.insert(0, "num1")

# extend() 列表合并
names.extend([1, 2, 3])

for i in range(10):
    ran = random.randint(1, 50)
    names.append(ran)

print("names:", names)

# 列表最大值
# max(<num list>)
# max_value = max(names)
# print("max_value", max_value)

# 列表最小值
# min(<num list>)

# 求总和
# sum(<num list>)

# sort() 排序 默认是升序
new_list = sorted([2, 1, 3, -1, 0])
print(new_list)

# 列表删除
# del list[index]

# remove 删除列表中第一次出现的元素, 返回结果是None, 如果没有找到会报异常

# pop(index) 默认移除列表中的最后一个元素 弹栈， 也可以指定index 删除

# clear() 里面的元素全部删除

# reverse() 反转

for i, value in enumerate(['lim', 'james', 'matt']):
    print(i, value)
"""
0 lim
1 james
2 matt
"""




