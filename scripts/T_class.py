import random
from functools import reduce


class People(object):
    def __init__(self, name="noname", gender=1):
        self.name = name
        self.__gender = gender

    def print_name(self):
        print("name is %s" % self.name)

    def get_gender(self):
        return self.__gender

    def print_gender(self):
        print ("gender is %s" % self.__gender)


class Student(People):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)

if __name__ == "__main__":
    p0 = People("lim", 0)
    p0.print_name()
    p0.name = "zhao si"
    print(p0.name, p0.get_gender())
    # 判断 p0 是否属于 People 类的实例
    print ("p0 属于gender %s" % isinstance(p0, People))