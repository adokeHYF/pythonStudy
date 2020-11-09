import random
import json

# 字典
"""
"""
dict1 = {}
dict2 = dict()
dict_people = {"ID": 1, "name": "张三", "age": 12}
# 新增
print(json.dumps(dict_people))

# 查看
# 通过[”key“] 方式取字典的值，如果key 不存在就会报错。
# 最好通过.get(<key>) 的方法取值，如果值不在的话，还可以设置默认值

if "xxx" not in dict_people:
    dict_people["xxx"] = "xxx"

if not dict_people.get("zzz"):
    dict_people["zzz"] = "zzz"

print(dict_people)

# 遍历字典
print("===== 遍历字典 =====")
for key in dict_people:
    print(f"key:{key}")

for key, value in dict_people.items():
    print(f"key:{key}, value:{value}")

# 更新 dict1.update(dict2)

# 内置函数 fromkeys(seq, [default]) ------> 如果没有指定默认的value则用None {'a': None, 'b': None}
seq_list = [1, 2, 3]
new_dict = dict.fromkeys(seq_list, None)
print(f"xxxx: {new_dict.get(1)}")


