from concurrent.futures import ProcessPoolExecutor
import os
import time


def task(n):
    print(f"start of thread{n} ..... {os.getlogin()}")
    time.sleep(5)
    print(f"end of the thread{n}......{os.getlogin()}")

y=time.process_time()
print(y)

with ProcessPoolExecutor(5) as exexutor:
    results=[exexutor.submit(task,_) for _ in range(6,0,-1)]


print(str(time.process_time() - y))


as
