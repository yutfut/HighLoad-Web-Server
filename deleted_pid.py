import os

start = 2412
finish = 2419

while start <= finish:
    os.system(f'sudo kill {start}')
    start += 1
