import random
from functools import reduce

"""
文件操作
   
"""


def file_operation(file_name):
    """
    文件操作
    :param file_name:
    :return: None
    """
    try:
        stream = open(f"F:\Practice\python\pythonStudy\\file\\" + file_name)
    except FileNotFoundError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        print("stream.buffer", stream.buffer)
        print("stream.read", stream.read())


if __name__ == "__main__":

    file_operation("test.txtt")



