fundametal/primitive data types:
------------------------------
int
float
bool
complex
str

bytes data type:
----------------
x = [10,20,30,40]
b = bytes(x)
print(type(b)) # bytes
1.  values is  0 to 256
2. immutable object


bytearray data type:
-------------------
x = [10,20,30,40]
b = bytearray(x)
print(type(b)) # bytearray
1. values should be 0 to 256
2. mutable.


bytes and bytearray are generally used to represent the images, videofiles and audiofiles.

list data type:
--------------
order is preserved
duplicates allowed
hetrogenous
scalable
repition operation is allowed x =[1,2,3]*2 # [1,2,3,1,2,3]
mutable

tuple data type:
---------------

list and tuple data types are exactly same but only tuple is immutable

range data type:
---------------

x = range(10)
x [10]
x[0:5]

immutable
slicing and indexing is applicable

range(10) # 0 to 9
range(10,50) # 10 to 49
range(10,30,5) # 10,15,20,25

set data type:
--------------
insertion order is not preserved
duplicates not allowed
hetrogenous allowed
set does not support indexing or slicing
mutable
scalable


frozenset data type:
----------------------
s = {1,2,3,4,5}
fs = fronzenset(s)

remaining all properties are same as set but only fronzenset is immutable


mutable and immutable:

list      and tuple
set       and fronzenset
dict      and str
bytearray and bytes
          and range()
 
