import time
import concurrent.futures
#start counting time
start =time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f"done sleeping.... {seconds},,second(s)"

with concurrent.futures.ProcessPoolExecutor() as executor:
    results=[executor.submit(do_something,1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())



#threads=[]
#for _ in range(10):
#    t1=threading.Thread(target=do_something,args=[1.5])
#    t1.start()
#    threads.append(t1)
#
#for th in threads:
#    th.join()


finish=time.perf_counter()

print(f'finsihed in {round(finish-start,2)} second(s)')
