# 类型转换
# str() int() list() dict() set() tuple()

# str ====> int, list, set, tuple
str1 = "abc123"
print(f"字符串转数字, 必须是数字字符串: {int(str1)}")
print(f"字符串转list: {list(str1)}")
# print(f"字符串转dict: {dict(str1)}")
print(f"字符串转set: {set(str1)}")
print(f"字符串转tuple: {tuple(str1)}")

# list ====> set(), tuple(), 可以转成字典[(key, value), (key, value)]

