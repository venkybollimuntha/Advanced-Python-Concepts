import multiprocessing as m
import time

def withdraw(amount,lock):
    for i in range(100):
        lock.acquire()
        amount.value = amount.value - 1
        lock.release()

def deposit(amount,lock):
    for i in range(100):
        lock.acquire()
        # the critical code is put between the lock.acquire() and lock.release() 
        amount.value = amount.value +1
        lock.release()


if __name__ == '__main__':
    lst = [5,8,2,9,3,6]
    amount = m.Value('i',200) # creating a shared variable for both process
    # i stands for integer and d stands for double.
    lock = m.Lock()
    # creating a lock object and pass it to the methods.
    p1 = m.Process(target=withdraw,args= (amount,lock))
    p2 = m.Process(target=deposit,args= (amount,lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # if there is no lock object you get the print value as 
    # greater or lesser amount in your account.
    # To solve this issue we can use multiprocessing lock.
    print(amount.value)