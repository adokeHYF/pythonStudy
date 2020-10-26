#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

root = tk.Tk()


def callback():
    print("~被调用了~")


# 创建一个顶级菜单
menubar = tk.Menu(root)

# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="文件", menu=filemenu)

# 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
editmenu = tk.Menu(menubar, tearoff=False)
editmenu.add_command(label="剪切", command=callback)
editmenu.add_command(label="拷贝", command=callback)
editmenu.add_command(label="粘贴", command=callback)
menubar.add_cascade(label="编辑", menu=editmenu)


# 创建一个弹出菜单
pop_menu = tk.Menu(root, tearoff=False)
pop_menu.add_command(label="撤销", command=callback)
pop_menu.add_command(label="重做", command=callback)

frame = tk.Frame(root, width=512, height=512)
frame.pack()


def popup(event):
    pop_menu.post(event.x_root, event.y_root)


# 绑定鼠标右键
frame.bind("<Button-3>", popup)

# 设置显示菜单栏
root.config(menu=menubar)
root.mainloop()
