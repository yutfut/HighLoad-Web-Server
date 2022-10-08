import os

start = 3058
finish = 3066

while start <= finish:
    os.system(f'sudo kill {start}')
    start += 1
