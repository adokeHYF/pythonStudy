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


def read_json_file():
    print(__file__)
    file_dir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    with open(os.path.join(file_dir, 'file\\test.json'), 'r', encoding='utf-8') as f:
        json_str = json.load(f)
        print(json_str)
        dict_f = json.loads('{"a":"b"}')
        print(dict_f)



if __name__ == "__main__":
    read_json_file()