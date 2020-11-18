from tkinter import Tk, Canvas
import time
import threading

windows = Tk()

canvas = Canvas(windows, height=500, width=500)

canvas.pack()
start1 = 30
start2 = 120
start3 = 210
start4 = 300

a = canvas.create_arc(400, 400, 100, 100, start=start1, extent=30, fill="red")
b = canvas.create_arc(400, 400, 100, 100, start=start2, extent=30, fill="red")
c = canvas.create_arc(400, 400, 100, 100, start=start3, extent=30, fill="red")
d = canvas.create_arc(400, 400, 100, 100, start=start4, extent=30, fill="red")


# 初始图象
def Draw():
    global start1
    global start2
    global start3
    global start4
    canvas.delete('all')  # 删除上一个图形
    start1 += 30
    start2 += 30
    start3 += 30
    start4 += 30
    a = canvas.create_arc(400, 400, 100, 100, start=start1, extent=30, fill="red")
    b = canvas.create_arc(400, 400, 100, 100, start=start2, extent=30, fill="red")
    c = canvas.create_arc(400, 400, 100, 100, start=start3, extent=30, fill="red")
    d = canvas.create_arc(400, 400, 100, 100, start=start4, extent=30, fill="red")


# 画出下一个图形
def delay():
    while 1:
        time.sleep(0.5)
        Draw()


# 延迟函数
if __name__ == '__main__':
    t = threading.Thread(target=delay)  # 开启线程
    t.start()
    windows.mainloop()
    t.join()