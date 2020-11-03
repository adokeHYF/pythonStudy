#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil
# description: 扑克牌游戏界面

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
        """ 通过place 布局实现游戏控制 """
        self.photos = [ImageTk.PhotoImage(Image.open(f"../icons/puke{i+1}.jpg")) for i in range(10)]
        self.pukes = [tk.Label(self.master, image=self.photos[idx]) for idx, value in enumerate(self.photos)]
        for idx, puke in enumerate(self.pukes):
            puke.place(x=10+idx*40, y=50)

        # 所有的Label 添加事件处理
        self.pukes[0].bind_class("Label", "<Button-1>", self.chuopai)

    def configWindow(self):
        self.master.title("扑克牌游戏")
        self.master.geometry("600x200+200+300")

    def chuopai(self, event):
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)

if __name__ == "__main__":
    window = tk.Tk()
    app = Application(master=window)
    window.mainloop()