import random
from functools import reduce


class People(object):
    # __slots__ = ("age", "addr", "name", "gender")
    def __init__(self, name="noname", gender=1, age=0):
        self.name = name
        self.__gender = gender
        self.age = age

    def print_name(self):
        print("name is %s" % self.name)

    def get_gender(self):
        return self.__gender

    def print_gender(self):
        print ("gender is %s" % self.__gender)

    @property
    def age_year(self):
        return self.age

    @age_year.setter
    def age_year(self, age):
        self.age = age


class Student(People):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)


if __name__ == "__main__":
    p0 = People("lim", 0)
    p0.print_name()
    p0.name = "zhao si"
    print(p0.name, p0.get_gender())
    stu1 = Student()
    # 判断 p0 是否属于 People 类的实例
    print ("p0 属于gender %s" % isinstance(p0, People))

    # 判断 stu1 是否属于 People 类的实例
    print("stu1 属于gender %s" % isinstance(stu1, People))

    # 输出类的属性
    print("p0 的属性 %s" % dir(p0))

    # 判断实例化的类是否含有某种属性
    print("p0 是否含有 __dir__ 方法：%s" % hasattr(p0, "__dir__"))

    #
    p0.age_year = 30
    print("%s is %s years old" % (p0.name, p0.age_year))