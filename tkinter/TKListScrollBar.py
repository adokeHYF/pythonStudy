#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


class AutomagicaTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tkFrame = None
        self.ttkFrame = None
        self.title("ScrollBar")
        self.geometry("1366x768")
        # Hide Tkinter root window
        # self.withdraw()
        self.config(bg="white")
        self.theLB = None
        self._layout()

    def _layout(self):
        # self.createTkScrollBar()
        self.createTTkScrollBar()

    def createTkScrollBar(self):
        scroll_bar = tk.Scrollbar(self)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        list_box = tk.Listbox(self)
        for i in range(1000):
            list_box.insert(tk.END, i)
        list_box.config(yscrollcommand=scroll_bar.set)
        list_box.pack(expand=1, fill=tk.BOTH)

    def createTTkScrollBar(self):
        canvas = tk.Canvas(self, width=250, scrollregion=(0, 0, 520, 2000))  # 创建canvas
        canvas.place(x=0, y=0, relheight=1)  # 放置canvas的位置
        frame = tk.Frame(canvas)  # 把frame放在canvas里
        tk.Label(frame, text="测试", bg="red").pack(side=tk.LEFT)
        frame.place(width=180, height=180)  # frame的长宽，和canvas差不多的
        vbar = tk.Scrollbar(canvas, orient=tk.VERTICAL)  # 竖直滚动条
        vbar.place(x=240, width=10, relheight=1)
        vbar.configure(command=canvas.yview)
        # hbar = tk.Scrollbar(canvas, orient=tk.HORIZONTAL)  # 水平滚动条
        # hbar.place(x=0, y=165, width=180, height=20)
        # hbar.configure(command=canvas.xview)
        # canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)  # 设置
        canvas.config(yscrollcommand=vbar.set)  # 设置
        canvas.create_window((50, 10), window=frame)  # create_window


app = AutomagicaTk()
app.mainloop()