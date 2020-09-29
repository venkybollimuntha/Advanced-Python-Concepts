from multiprocessing import Pool

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum 

if __name__ == '__main__':
    array = [i for i in range(100000)]
    t1 = time.time()
    p = Pool(processes=3) # processess arrtibute is optional, 
    # at a time it will use only 3 process.
    p.map(f,array) # this will distribute the work to all the CPU cores.
    p.close()
    p.join() # this is must, then only it will collect all the process results.


    print("pool took",time.time()-t1)


    t2 = time.time()

    result = []
    for n in array: 
        result.append(f(n))

    print("serial proccessing took",time.time()-t2)



#######################Example2#############################################
import multiprocessing
from itertools import product

def merge_names(a, b):
    return '{} & {}'.format(a, b)

if __name__ == '__main__':
    names = ['Brown', 'Wilson', 'Bartlett', 'Rivera', 'Molloy', 'Opie']
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.starmap(merge_names, product(names, repeat=2))
        # repeat = 2 means your function accepting inputs.
        # if you give repeat as 3, your function must accept 3 inputs.
    print(results)

# Output: ['Brown & Brown', 'Brown & Wilson', 'Brown & Bartlett', ...