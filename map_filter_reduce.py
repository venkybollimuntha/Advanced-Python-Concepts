Note:
# Map is used to pass each value to the function in the list and compute the results in a single line
# Filter is used to Remove/filter the values based on condition, in the list or iterable object
# Reduce is used to remember the previous value like (x+=1, x*=x) and return the value 
# We have to import the reduce funtion from the functools.
# map and filter return the objects, we need to convert it to list to see the output.





# Map (mapping or passing each element once with function)

#all are used to do the manipulation of list object or iterable object


# syntax:      list(map(function, iterable))


def area(r):
    return 22/7 *(r**r)

print(list(map(area,range(10))))

# for each value in the range sequence, we need to apply area function, map will do that for
# us


# filter: (to filter unwanted values in the list we can use filter)
# ------

# syntax:   filter(function,iterable)

lst = [1,2,3,"","hello","we",'want',"","apple","welcome",3,5,6]

print(list(filter(None,lst)))
# It will fiter the empty value in the list and returns pure list

# Flase values in python:

# "", 0,0.0, None, [], {}, (), False,0j,

data = [1,100,30,50,44,79,83,150,250]

print(list(filter(lambda x: x >100, data)))


# Reduce (x =x+1 or to remember previous values we can use reduce function)
# syntax: reduce(function,iterable)

from functools import reduce

data = [1,2,3,4,5,6,7,8,9]

print(reduce(lambda x,y:x*y,data))

