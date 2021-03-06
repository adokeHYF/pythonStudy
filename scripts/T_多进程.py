import random
from functools import reduce
import os
from multiprocessing import Process, Pool, cpu_count
import subprocess
import time
import platform

__auth__ = "abeil"
"""
Pool 是个进程池子, 依靠于主进程存在, 如果主进程结束, 无论线程池里面有多少个线程未完成或者正在完成,
都会结束, 非阻塞式.

进程池特点:
    设置进程数量
    进程的复用
    非阻塞式

非阻塞式:全部添加到队列中,立刻返回,并没有等待其他进程执行完毕后才会返回,但是回调函数等待任务完成后才会调用
阻塞式: 添加一个执行一个任务，如果一个任务不结束另一个任务就进不来
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
    print(f'Process ({os.getpid()}) start...')
    system = platform.system()
    print(f"system: {system} \ncpu 核数: {cpu_count()}")
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

