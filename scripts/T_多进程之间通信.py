import random
from functools import reduce
import os
from multiprocessing import Process, Pool, cpu_count, Queue
import subprocess
import time
import platform

__auth__ = "abeil"
"""
队列：先进先出（FIFO）
栈：后进先出
"""


def run_proc_windows(name):
    print(f"windows run {name}  process")


def long_time_task(name):
    print('Run task %s (%s)...父进程: %s' % (name, os.getpid(), os.getppid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    return 'Task %s runs %0.2f seconds.' % (name, (end - start))


def callback_fun(n):
    print(n)


if __name__ == "__main__":
    system = platform.system()
    q = Queue(5)
    q.put(1)

    if system == "Windows":
        # 创建一个子进程
        p = Process(target=run_proc_windows, args=('test',))
        print('子进程将开始')
        p.start()
        p.join()
        print('子进程结束 \n')
        # 初始化进程池
        p = Pool(8)
        for i in range(10):
            # 非阻塞式
            # p.apply_async(long_time_task, args=(i,), callback=callback_fun)

            # 阻塞式
            p.apply(long_time_task, args=(i,))

        print('等待子进程运行...')
        p.close()
        p.join()
        print('所有进程运行完毕.')

    else:
        pid = os.fork()
        if pid == 0:
            print(f'I am child process ({os.getpid()}) and my parent is ({os.getppid()}).')
        else:
            print(f'I ({os.getpid()}) just created a child process ({pid}).')

