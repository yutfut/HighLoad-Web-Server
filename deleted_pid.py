import os

start = 7514
finish = 7522

while start <= finish:
    os.system(f'sudo kill {start}')
    start += 1
