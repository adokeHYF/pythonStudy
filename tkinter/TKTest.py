#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

"""
# def button_press():
#     pass
#
#
# def callback(event):
#     label.focus_set()
#     print("click at", event.x, event.y)
#
#
# def closeWindow():
#     if tk.messagebox.askokcancel("Quit", "你是否想退出"):
#         window.destroy()
#
#
# def menuCallBack():
#     print('menu call back')
#
#
# window = tk.Tk()
# window.title("主窗体")
# window.geometry("1366x768")
#
# # 主窗体里面添加一个新的菜单栏
# menu = tk.Menu(window)
# window.config(menu=menu)
# file_menu = tk.Menu(menu)
# file_menu.add_command(label='New', command=menuCallBack)
# file_menu.add_separator()
# file_menu.add_command(label='Quit', command=closeWindow)
# menu.add_cascade(label="File", menu=file_menu)
#
# edit_menu = tk.Menu(menu)
# edit_menu.add_command(label="Cut", command=menuCallBack)
# file_menu.add_separator()
# edit_menu.add_command(label="Copy", command=menuCallBack)
# menu.add_cascade(label="Edit", menu=edit_menu)
#
# # 主窗体添加一个topBar
# toolBar = tk.Frame(window)
# t_btn1 = tk.Button(toolBar, width=6, text="file")
# t_btn1.pack(side=tk.LEFT, padx=2, pady=2)
# t_btn2 = tk.Button(toolBar, width=6, text="save as")
# t_btn2.pack(side=tk.LEFT, padx=2, pady=2)
# toolBar.pack(side=tk.TOP, fill=tk.X)
#
# # 主窗体里面添加一个新的label
# label = tk.Label(window, text="Hello World")
# label.config(cursor="gumby", width="100", height="10", fg="yellow", bg="dark green")
# label.config(font=("Times", "28", "bold"))
# # bind event
# label.bind("<Button-1>", callback)
# label.pack()
#
# # 主窗体中添加StatusBar
# status_bar = tk.Label(window, text="Len", relief=tk.SUNKEN, bd=2, anchor=tk.W)
# status_bar.pack(side=tk.BOTTOM,fill=tk.X)
#
#
# # # 添加一个新的窗体
# # top = tk.Toplevel()
# # top.title("top level")
#
# # 表格布局
# style = ttk.Style()
# style.configure("BW.TLabel", foreground="black", background="white")
#
# table_frame = tk.Frame(window)
#
# tk.Label(table_frame, text="Name").grid(row=1, column=1)
# tk.Label(table_frame, text="Address").grid(row=2, column=1)
#
# ttk.Label(table_frame, text="Test", style="BW.TLabel").grid(row=1, column=2)
# ttk.Label(table_frame, text="Test", style="BW.TLabel").grid(row=2, column=2)
# table_frame.pack(fill=tk.X)
#
#
# # 协议绑定事件
# window.protocol("WM_DELETE_WINDOW", closeWindow)
# # 主窗口循环显示
# window.mainloop()
"""


def event_callback(type):
    if type == 1:
        print("menu callBack")
    elif type == 2:
        print("close window")
    elif type == 3:
        print("callback")
    else:
        print("other callback")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # 菜单栏
        self.menu = None
        self.file_menu = None
        self.edit_menu = None
        # topBar
        self.toolBar = None
        self.master.title("测试窗体")
        self.master.geometry("1366x768")
        self.pack()
        self.create_menu()
        self.create_top_bar()
        self.create_container()
        self.create_status_bar()

    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu)
        self.file_menu.add_command(label='New', command=event_callback(1))
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Quit', command=event_callback(2))
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu)
        self.edit_menu.add_command(label="Cut", command=event_callback(1))
        self.file_menu.add_separator()
        self.edit_menu.add_command(label="Copy", command=event_callback(1))
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)

    def create_top_bar(self):
        self.toolBar = tk.Frame(self.master, borderwidth=2, padx=5, pady=5, relief=tk.GROOVE)
        t_btn1 = tk.Button(self.toolBar)
        # 正常设置
        t_btn1.config(width=10, height=1, text="file", cursor="hand2", bg="yellow", borderwidth=0,
                      highlightbackground="red", takefocus=True, relief=tk.FLAT)
        t_btn1.pack(side=tk.LEFT, padx=2, pady=2)

        # width height 用像素设置, 必须利用 image 属性设置
        pixelVirtual = tk.PhotoImage(width=1, height=1)
        t_btn2 = tk.Button(self.toolBar, image=pixelVirtual, width=80, height=20, text="save as", compound=tk.CENTER)
        t_btn2.pack(side=tk.RIGHT, padx=2, pady=2)
        self.toolBar.pack(side=tk.TOP, fill=tk.X)

    def create_button_width_pixel(self):
        # 主窗体里面添加一个新的label
        label = tk.Label(self.master, text="Hello World")
        label.config(cursor="gumby", width="100", height="10", fg="yellow", bg="dark green")
        label.config(font=("Times", "28", "bold"))
        # bind event
        label.bind("<Button-1>", event_callback(4))
        label.pack()

    def create_status_bar(self):
        # 主窗体中添加StatusBar
        status_bar = tk.Label(self.master, text="Len", relief=tk.SUNKEN, bd=2, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_container(self):
        self.container = tk.Frame(self.master, bd=1, relief=tk.SUNKEN, bg="pink")\
             .pack(fill=tk.BOTH, expand=tk.YES)
        self.slide_bar = tk.Frame(self.container, relief=tk.SUNKEN, bg="red", width=100).pack(fill=tk.Y, side=tk.LEFT)
        # var = tk.IntVar()
        # cbtn1 = tk.Checkbutton(self.master, text="Expand", variable=1).pack(side=tk.LEFT)
        # cbtn2 = tk.Checkbutton(self.master, text="Expand1", variable=2).pack(side=tk.LEFT)
        # # separator = tk.Frame(self.master, height=100, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)


    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack()

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)

# 表格布局
# style = ttk.Style()
# style.configure("BW.TLabel", foreground="black", background="white")
#
# table_frame = tk.Frame(root)
#
# tk.Label(table_frame, text="Name").grid(row=1, column=1)
# tk.Label(table_frame, text="Address").grid(row=2, column=1)
#
# ttk.Label(table_frame, text="Test", style="BW.TLabel").grid(row=1, column=2)
# ttk.Label(table_frame, text="Test", style="BW.TLabel").grid(row=2, column=2)
# table_frame.pack(fill=tk.X)

app.mainloop()