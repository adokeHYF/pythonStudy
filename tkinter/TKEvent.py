#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil
# description: 键盘鼠标事件

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import Image, ImageTk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configWindow()
        self.createWidget()
        self.pack()

    def createWidget(self):
        self.test_label = tk.Label(self, text="键盘鼠标事件测试")
        self.test_label.bind("<Enter>", self._test_event)
        self.test_label.pack()

    def _test_event(self, event):
        self.test_label.focus_set()
        self.test_label.bind("<Delete>", self._event_delete)
        print(event)

    def _event_delete(self, event):
        print("delete")

    def configWindow(self):
        self.master.title("扑克牌游戏")
        self.master.geometry("600x200+200+300")


if __name__ == "__main__":
    window = tk.Tk()
    app = Application(master=window)
    window.mainloop()