#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


window = tk.Tk()

# 设置工具栏
toolBar = tk.Frame(window, borderwidth=2, padx=5, pady=5, relief=tk.GROOVE)
t_btn1 = tk.Button(toolBar)
# 正常设置
t_btn1.config(width=10, height=1, text="file", cursor="hand2", bg="yellow", borderwidth=0,
              highlightbackground="red",takefocus=True, relief=tk.FLAT)
t_btn1.pack(side=tk.LEFT, padx=2, pady=2)

# width height 用像素设置, 必须利用 image 属性设置
pixelVirtual = tk.PhotoImage(width=1, height=1)
t_btn2 = tk.Button(toolBar, image=pixelVirtual, width=80, height=20, text="save as", compound=tk.CENTER)
t_btn2.pack(side=tk.RIGHT, padx=2, pady=2)
toolBar.pack(side=tk.TOP, fill=tk.X)

# status_bar = tk.Frame(window, relief=tk.SUNKEN, bg="green", height=50).pack(side=tk.BOTTOM, fill=tk.X)

# 设置内容
# slide_bar_left = tk.Frame(window, relief=tk.SUNKEN, bg="red", width=200).pack(fill=tk.Y, side=tk.LEFT, expand=tk.YES)
container = tk.Frame(window, bd=1, relief=tk.SUNKEN, width=966)

# slide_bar_right = tk.Frame(window, relief=tk.SUNKEN, bg="blue", width=200).pack(fill=tk.Y, side=tk.RIGHT)


t_btn3 = tk.Button(container, image=pixelVirtual, width=100, height=100, text="container")
t_btn3.pack(side=tk.LEFT)
container.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT)



# 协议绑定事件
# window.protocol("WM_DELETE_WINDOW", closeWindow)
# 主窗口循环显示
window.title("测试窗体")
window.geometry("1366x768")
window.mainloop()
