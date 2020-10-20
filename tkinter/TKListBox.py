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
        self.title("CheckButton")
        self.geometry("1366x768")
        self.is_checked = tk.StringVar()
        # Hide Tkinter root window
        # self.withdraw()
        # self.config(padx=5, pady=5)
        self.theLB = None
        self._layout()

    def _layout(self):
        self.createTkCheckButton()
        self.createTtkCheckButton()

    def createTkCheckButton(self):
        self.is_checked.set('no')
        self.tkFrame = tk.Frame(self, bd=3, relief=tk.RIDGE, height=200)
        tk.Label(self.tkFrame, text="tk", height=5).pack(side=tk.LEFT, padx=20)

        self.theLB = tk.Listbox(self.tkFrame, setgrid=True)

        # 往列表里添加数据
        for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
            self.theLB.insert("end", item)
        self.theLB.pack(side=tk.LEFT)

        self.tkFrame.pack(fill=tk.X)

    def createTtkCheckButton(self):
        self.ttkFrame = tk.Frame(self, bd=3, relief=tk.RIDGE, height=150)
        tk.Label(self.ttkFrame, text="ttk", height=5).pack(side=tk.LEFT, padx=20)
        self.ttkFrame.pack(fill=tk.X, side=tk.TOP)

    def get_checkbutton_value(self):
        print("是否点击", self.is_checked.get())


app = AutomagicaTk()
app.mainloop()