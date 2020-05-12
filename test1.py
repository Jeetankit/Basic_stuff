#this module provides a high level API for executing asynchronus task
import concurrent.futures

#executor class is an abstract class and cannot be used directly
#The two subclass can be imported which are
#Number 1-------
concurrent.futures.ThreadPoolExecutor
#This class has pools of th thread and use the multithreading

concurrent.futures.ProcessPoolExecutor

#This class has pools of process and use the muliporocessing
#we get a pool of threads or process and submit task to these pool
#it will automatically the assigne the task to the available resource and schedule them torun


from time import sleep


def task(message):
    print("start task")
    sleep(5)
    print(message)

pool=concurrent.futures.ThreadPoolExecutor(3)

future=pool.map(task,["hell0","nothing","couldbe"])
