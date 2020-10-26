
def raise_1():
    raise


def raise_2():
    raise ZeroDivisionError


def raise_3():
    raise ZeroDivisionError("除数不能为零")


if __name__=='__main__':
    # raise_1()
    # raise_2()
    raise_3()