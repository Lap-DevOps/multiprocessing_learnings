import os
import time
import multiprocessing

print(f'Start from process ID = {os.getpid()}')


def task(n=1_000_000_000):
    while n:
        n -= 1


if __name__ == '__main__':
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'Running for  {finish - start: .2f} seconds.')
