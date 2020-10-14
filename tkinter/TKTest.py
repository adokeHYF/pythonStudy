#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


def button_press():
    pass


def callback(event):
    label.focus_set()
    print("click at", event.x, event.y)


def closeWindow():
    if tk.messagebox.askokcancel("Quit", "你是否想退出"):
        window.destroy()


def menuCallBack():
    print('menu call back')


window = tk.Tk()
window.title("主窗体")
window.geometry("1366x768")

# 主窗体里面添加一个新的菜单栏
menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu)
file_menu.add_command(label='New', command=menuCallBack)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=closeWindow)
menu.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu)
edit_menu.add_command(label="Cut", command=menuCallBack)
file_menu.add_separator()
edit_menu.add_command(label="Copy", command=menuCallBack)
menu.add_cascade(label="Edit", menu=edit_menu)

# 主窗体添加一个topBar
toolBar = tk.Frame(window)
t_btn1 = tk.Button(toolBar, width=6, text="file")
t_btn1.pack(side=tk.LEFT, padx=2, pady=2)
t_btn2 = tk.Button(toolBar, width=6, text="save as")
t_btn2.pack(side=tk.LEFT, padx=2, pady=2)
toolBar.pack(side=tk.TOP, fill=tk.X)

# 主窗体里面添加一个新的label
label = tk.Label(window, text="Hello World")
label.config(cursor="gumby", width="100", height="10", fg="yellow", bg="dark green")
label.config(font=("Times", "28", "bold"))
# bind event
label.bind("<Button-1>", callback)
label.pack()

# 主窗体中添加StatusBar
status_bar = tk.Label(window, text="Len", relief=tk.SUNKEN, bd=2, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM,fill=tk.X)

# 表格布局
tk.Label(window, text="Name").grid(row=1)
tk.Label(window, text="Address").grid(row=2)


# 添加一个新的窗体
# top = tk.Toplevel(bg="red")
# top.title("top level")


# 协议绑定事件
window.protocol("WM_DELETE_WINDOW", closeWindow)
# 主窗口循环显示
window.mainloop()
