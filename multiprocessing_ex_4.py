import datetime
import multiprocessing
import os
import time


def sleeper():
    time.sleep(10)
    print(f'Child process {os.getpid()} has been finised!')


if __name__ == '__main__':
    start = datetime.datetime.now()
    p = multiprocessing.Process(target=sleeper)
    p1 = multiprocessing.Process(target=sleeper)
    p.start()
    p1.start()
    p.join()
    p1.join()
    print(f"Program in maim process {os.getpid()} has been finished! Total execution time: ",
          datetime.datetime.now() - start)
