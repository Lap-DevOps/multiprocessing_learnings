import multiprocessing
from random import random
from time import sleep


def releaser(l):
    print('Stop child process')
    l.release


def file_writer(start: int, finish: int):
    with open('locker.txt', 'a') as file:
        for i in range(start, finish):
            sleep(random())
            print(i)
            file.write(f'{i}\n')


def bed_file_writer(start: int, finish: int, l: multiprocessing.Lock()):
    l.acquire()
    for i in range(start, finish):
        with open('locker_bed.txt', 'a') as file:
            sleep(random())
            print(i)
            file.write(f'{i}\n')
    p = multiprocessing.Process(target=releaser, args=(l,))
    p.start()


if __name__ == '__main__':
    lock = multiprocessing.Lock()
    # p1 = multiprocessing.Process(target=file_writer, args=(0, 5))
    # p2 = multiprocessing.Process(target=file_writer, args=(5, 10))
    p3 = multiprocessing.Process(target=bed_file_writer, args=(0, 5, lock))
    p4 = multiprocessing.Process(target=bed_file_writer, args=(5, 10, lock))
    # p1.start()
    # p2.start()
    p3.start()
    p4.start()
    p3.join()
    p4.join()
