#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil

import tkinter as tk
from tkinter import ttk


def button_press():
    pass


window = tk.Tk()
# window.geometry("1366x768")
main_frame = ttk.Frame(window, padding="3 3 12 12")
main_frame.grid()
button = ttk.Button(main_frame, text="Hello World", command=button_press)
button.grid(column=3, row=3, sticky=tk.W)
# 主窗口循环显示
window.mainloop()
