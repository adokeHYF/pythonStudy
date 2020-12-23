#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

from PIL import ImageTk, Image


class AutomagicaTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Canvas")
        self.geometry("1000x800")
        self.resizable(width=False, height=False)
        # Hide Tkinter root window
        # self.withdraw()
        self.canvas = None
        self._layout()

        # self.canvas.bind("<ButtonPress-1>", self.move_start)
        # self.canvas.bind("<B1-Motion>", self.move_move)

    def _layout(self):
        self.create_canvas()
        # self.create_arc()

    def create_canvas(self):
        self.canvas = tk.Canvas(self, background='white', bd=0)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        # # 画线
        # self.create_line()
        # 创建图片
        self.create_image()

    def create_range(self):
        self.canvas.create_rectangle(
            30, 30, 200, 200,
            outline='red',
            fill="red",
            width=5,
            activedash=True,
            dash=(5,),
            tags="background"
        )

    def create_line(self):
        for i in range(0, 1050, 50):
            # 竖线
            self.canvas.create_line(i, 0, i, 1000, dash=(4, 2), tag="grid_line", fill="red", tags="background",)

        for i in range(0, 800, 50):
            # 横线
            self.canvas.create_line(0, i, 1000, i, dash=(4, 2), tag="grid_line", fill="green", tags="background", )

    def create_arc(self):
        self.canvas.create_rectangle(100, 100, 200, 200)
        # 右半圆
        self.canvas.create_arc(150, 100, 250, 200)
        self.canvas.create_arc(150, 100, 250, 200, start=-90, extent=180)
        # # 左半圆
        self.canvas.create_arc(50, 100, 150, 200, start=90, extent=180)

    def create_image(self):
        """
        tk canvas 中要插入图片必须先生成图片后，将该图片附在一个python CG 系统不会自动回收的变量上，不然系统会将图片自动回收，不会在canvas 中显示
        """
        img = Image.open(f"../icons/puke1.jpg")
        self.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor='nw', image=self.image)
        print(self.__class__.__name__)


    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)


if __name__ == "__main__":

    root = AutomagicaTk()
    root.mainloop()

