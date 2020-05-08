import time
import concurrent.futures
#start counting time
start =time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f"done sleeping.... {seconds},,second(s)"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    results=executor.map(do_something,secs)

    for result in results:
        print(result)


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
