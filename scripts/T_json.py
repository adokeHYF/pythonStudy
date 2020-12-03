#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

"""
json.load()从文件中读取json字符串

json.loads()将json字符串转换为字典类型

json.dumps()将python中的字典类型转换为字符串类型

json.dump()将json格式字符串写到文件中
"""

file_dir = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )


def white_file(num):
    print('开始写入')
    with open(os.path.join(file_dir, 'file\\read.txt'), 'w', encoding='utf-8') as f:
        for i in range(num):
            f.write(str(i))

    print('写入完毕')


def read_json_file():
    print('开始读取')
    with open(os.path.join(file_dir, 'file\\read.txt'), 'r', encoding='utf-8') as f:
        print(f.read())
        # json_str = json.load(f)
        # print(json_str)
        # dict_f = json.loads('{"a":"b"}')
        # print(dict_f)
    print('读取完毕')


if __name__ == "__main__":
    white_file(10)
    read_json_file()