import os

print(f'Start from process ID = {os.getpid()}')

nun_proc = int(input('How many processes ? '))

for i in range(nun_proc):

    pid = os.fork()
    print(f'i = {i}')
    if pid != 0:
        print(f'running process {pid} from main process {os.getpid()}')
print(f'*** continue process {os.getpid()}')
