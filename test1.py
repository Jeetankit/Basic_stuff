from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os
import time


def task(n):
    print(f"start of thread{n} ..... {os.getlogin()}......{os.ctermid()}")
    time.sleep(3)
    print(f"end of the thread{n}......{os.getlogin()}")

y=time.process_time()
print(y)

with ProcessPoolExecutor(5) as exexutor:
    results=[exexutor.submit(task,_) for _ in range(5,0,-1)]

with open("ankit.txt","a")as a:
    a.write(str(results))


#print(str(time.process_time() - y))
