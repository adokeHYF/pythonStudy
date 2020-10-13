#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil

import tkinter as tk
from tkinter import ttk


def button_press():
    pass


# Initialize style
s = ttk.Style()
s.configure('Frame1', background='red')


window = tk.Tk()
window.geometry("1366x768")
window.title("TTK TEST")
main_frame = tk.Frame(window, width="100", height="100")
main_frame.pack()
label= tk.Label(main_frame,text="Label",justify=tk.LEFT)
label.pack(side=tk.LEFT)
# button = ttk.Button(main_frame, text="Hello World", command=button_press)
# button.grid(column=3, row=3, sticky=tk.W)
# 主窗口循环显示
window.mainloop()
