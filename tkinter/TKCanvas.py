#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Abeil

import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


class AutomagicaTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Canvas")
        self.geometry("1366x768")
        # Hide Tkinter root window
        # self.withdraw()
        self.canvas = None
        self._layout()

    def _layout(self):
        self.create_canvas()

    def create_canvas(self):
        self.canvas = tk.Canvas(self, background='white', bd=0)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.canvas.create_rectangle(
            30, 30, 200, 200,
            outline='red',
            fill="red",
            width=5,
            activedash=True,
            dash=(5,)
        )


if __name__ == "__main__":
    root = AutomagicaTk()
    root.mainloop()
