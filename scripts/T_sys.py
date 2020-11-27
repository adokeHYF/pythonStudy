#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def print_args():
    for idx, arg in enumerate(sys.argv):
        print(f"参数{idx}: {arg}")


if __name__ == "__main__":
    print_args()