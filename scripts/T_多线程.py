import random
from functools import reduce
import os
from multiprocessing import Process, Pool, cpu_count
import subprocess
import time
import threading
import platform

__auth__ = "abeil"


def run_proc_windows(name):
    print(f"windows run {name}  process")


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


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
            p.apply_async(long_time_task, args=(i,))

        print('等待子进程运行...')
        p.close()
        p.join()
        print('所有进程运行完毕.')

        print('$ nslookup www.python.org')
        r = subprocess.call(['nslookup', 'www.python.org'])
        print('Exit code:', r)



    else:
        pid = os.fork()
        if pid == 0:
            print(f'I am child process ({os.getpid()}) and my parent is ({os.getppid()}).')
        else:
            print(f'I ({os.getpid()}) just created a child process ({pid}).')

