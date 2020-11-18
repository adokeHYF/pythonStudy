import random

a = 100


def func():
    b = 20

    def inner_func():
        nonlocal b
        global a
        c = 30
        b += 20
        a += 80
        print(f"locals-{locals()}")

    inner_func()
    print(a, b)
    print(f"locals-{locals()}")


if __name__ == "__main__":
    func()
    print(f"globals-{globals()}")
