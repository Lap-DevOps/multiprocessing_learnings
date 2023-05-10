import multiprocessing
from multiprocessing import Process

import os
import time

CNT = 0


def foo():
    global CNT
    print(f'foo started from -: {os.getpid()}')
    time.sleep(3)
    CNT += 2
    print(f'f: = {CNT} from  {os.getpid()} ')


if __name__ == '__main__':
    p = Process(target=foo, args=())
    p1 = multiprocessing.Process(target=foo, args=())
    p2 = multiprocessing.Process(target=foo, args=())

    p.start()
    p1.start()
    p2.start()
