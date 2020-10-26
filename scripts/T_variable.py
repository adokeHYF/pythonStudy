"""
    变量类型: 字符串, 整形, 浮点数, 布尔类型, 列表list, 字典(无序字典, 有序字典) set列表(不存重复数据的列表)
    变量命名规则: 正常变量->驼峰/下划线, 类变量-> 大驼峰, 常量->全大写
"""

# 字符串
name = "李明"

# 整形
age = 120

# 浮点数
salary = 111.11

# 布尔类型
isMan = True

"""
格式化输出
    %s: string
    %d: number
    %f: float
    
    1. 使用占位符
    print("姓名叫: %s, %i岁了, 工资是%.2f" % (name, age, salary))
    
    2. format
    print("姓名叫: {}, {}岁了, 工资是{}".format(name, age, salary))
    
"""

print("姓名叫: %s, %i岁了, 工资是%.2f" % (name, age, salary))
print("姓名叫: {}, {}岁了, 工资是{}".format(name, age, salary))

