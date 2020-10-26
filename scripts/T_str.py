import random
msg = "Zhou is pig"
# <string>.title()
print(msg.title())
# <string>.istitle()
print(msg.istitle())
# <string>.capitalize()
print(msg.capitalize())
# <string>.islower()
print(msg.islower())
# <string>.lower()
print(msg.lower())
# <string>.isupper()
print(msg.isupper())
# <string>.upper()
print(msg.upper())

# 验证码
allCheckStr = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
checkMark = ""
for i in range(4):
    checkMark += allCheckStr[random.randint(0, len(allCheckStr) - 1)]
print('checkMark: %s'%(checkMark))

# 查找相关的, 替换
# <string>.find('str', start(int), end(int)) 返回索引, 如果是-1, 则是没有找到。否则返回第一个符合str 的索引 等同于js 的 search
checkMark.find('l', 0, 3)

# <string>.lfing()

# <string>.rfind()

# <string>.index()

# <string>.rindex()

# <string>.lindex()

# <string>.replace()

# 编码和解码
# encode 编码
msg = "你好 世界"
result = msg.encode("utf-8")
print("你好世界:%s"%(result))
# decode 解码
print("解码:%s"%(result.decode("utf-8")))

# startwidth() endwidth() 返回类型都是布尔值的True, False
# 应用文件上传
file_name = "笔记.txt"
print("%s 是以txt结尾吗%s: "%(file_name, file_name.endswith("txt")))

# 保留格式
print(r"\rth")

# isaplha() 是否是字母 isdigit() 是否是数字

# join 字符串连接
# new_str = '_'.join('abc') # a_b_c
list = ['a', 'b', 'c']
new_str = '_'.join(list)

# 去除空格
# lstrip() rstrip() strip()
# print('  a_b_c  '.strip())

# 分割字符串
# splite('分隔符', '次数')

# 字符串个数
# count()

"""
输入两个字符串，从第一个字符串中删除第二个字符串中所有的字符
"""
s1 = input("请输入第一个字符串: ")
s2 = input("请输入第二个字符串: ")
for i in s2:
    s1 = s1.replace(i, "")
print(s1)



