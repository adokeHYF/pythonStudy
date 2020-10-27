import random
"""
 运算符种类：
    1. 赋值运算符 = += -= *= /= %=
    2. 算数运算符 + - * / % **
    3. 关系运算符 == !=  > >= < <= is is not
    4. 逻辑运算符
    5. 位运算符
    6. 三目运算符： 和 js 一样

 运算符优先级(优先级高度从上到下)：
    运算符说明	Python运算符	                优先级	结合性	优先级顺序
    小括号	    ( )	                        19	        无	    高
    索引运算符	x[i] 或 x[i1: i2 [:i3]]	    18	        左
    属性访问	    x.attribute	                17	        左
    乘方	**	                                16	        左
    按位取反	~	                            15	        右
    符号运算符	+（正号）、-（负号）	        14	        右
    乘除	*、/、//、%	                        13	        左
    加减	+、-	                            12	        左
    位移	>>、<<	                            11	        左
    按位与	&	                            10	        右
    按位异或	^	                            9	        左
    按位或	|	                            8	        左
    比较运算符	==、!=、>、>=、<、<=          7	        左
    is 运算符	is、is 1
    not	                                    6	        左
    in 运算符	in、not in	                5	        左
    逻辑非	not	                            4	        右
    逻辑与	and	                            3	        左
    逻辑或	or	                            2	        左
    逗号运算符	exp1, exp2	                1	        左     低

"""
# while 循环
"""
num = input("请输入参数:")
radom_num = random.randint(1, 10)
while int(num) != radom_num:
    print("没猜中")
    num = input("请输入参数:")
    radom_num = random.randint(1, 10)
    print("num is %s, random_num is %s" % (str(num), str(radom_num)))
print("猜中了")
"""

# for 循环
"""
for i in range(1, 7):
    if i == 6:
        print("有6, 跳出循环")
        break
else:
    print("循环完成, 没有6")
"""

# 字符串
str1 = "hello" 
str2 = "hello word"
print(str1 in str2)

