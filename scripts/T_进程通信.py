import random
from functools import reduce
import os
from multiprocessing import Process, Pool, cpu_count, Queue
import subprocess
import time
import platform

__auth__ = "abeil"


def write(q):
    print(f'写进程: {os.getpid()}')
    for value in ['A', 'B', 'C']:
        print(f'Put {value} to queue...')
        q.put(value)
        time.sleep(random.random() * 3)


def read(q):
    print(f'读进程: {os.getpid()}')
    while True:
        value = q.get(True)
        print(f'Get {value} from queue.')


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

