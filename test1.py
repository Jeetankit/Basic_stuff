from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os
import time
import pygeocoder


def task(n):
    print(f"start of thread{n} ..... ")
    time.sleep(3)
    print(f"end of the thread{n}......")

with ProcessPoolExecutor(5) as exexutor:
    results=[exexutor.submit(task,_) for _ in range(5,0,-1)]

#nothing is memorable
