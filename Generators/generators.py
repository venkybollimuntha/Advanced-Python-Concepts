# Generators:

# Generators are lazily-evaluated iterators that render items only when requested, and thus they’re very memory efficient. 
# They should be used when you’re dealing with a large amount of data sequentially.



# l = [x*x for x in range(100000000000000000000000000000000000000000000000000000)]

# list comprehension will give memory error. because it will load all the elements to the memory

l = (x*x for x in range(100000000000000000000000000000000000000000000000000000))
# tuple comprehension is internally implemented on Generators.

print(type(l))  # gives generator class

print(next(l))
print(next(l))
print(next(l))
print(next(l))

# First example
def firstn(num):
    n = 1
    while n <=num:
        yield n
        n +=1

for i in firstn(10):
    print(i)

# Second Example
def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
for i in fib():
    if i >100:
        break
    print(i)


Advantages:
1. Memory utilization 
2. process time reduced.
