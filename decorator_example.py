
"""
Decorator:
----------
A decorator function is used to change or extend the behaviour of other functions. and they let you do that without permeanently modifying the wrapped function.
"""

######################  Example1 ###################################
# This time_it decorator calculate the time took to execute
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time took is ",end-start)
        return result
    return wrapper

@tiem_it
def squares():
	for i in range(1000000):
		pass # we are not intrested in output, we want to test time_it decorator

squares() # Time took is 0.013 seconds


############## Example2: (Modify function behaviour) ###################

def uppercase(func):
	def wrapper():
		result = func()
		modifying_result = result.upper()
		return modifying_result
	return wrapper

@uppercase
def my_fun():
    s = "Venky Bollimuntha"
    return s

print(my_fun()) # VENKY BOLLIMUNTHA

################### Example 3: (Multiple decorators to single function)######

def h1_tag(func):
	def wrapper():
		return "<h1>" + func() + "</h1>"
	return wrapper

def para_tag(func):
	def wrapper():
		return "<p>" + func() + "</p">
	return wrapper

@h1_tag
@para_tag
def my_tag():
# first para_tag is excecuted, then h1_tag is executed.
	return "Hello! Venky"

my_tag() # Hello! Venky in paragraph tag
# Hello! Venky in Header tag

#############  Example 4 (function that accept arguments) ############
def proxy(func):
	def wrapper(*args, **kwargs):
		result = func(*args,**kwargs)
		return result.upper()
	return wrapper

@proxy
def upper(s):
	return s

print(upper("venky bollimuntha")) # VENKY BOLLIMUNTHA


############   Example 5 (using import functool.wraps) (Recommended) #########
"""
Applying functools.wraps to the wrapper closure returned by the decorator carries over the docstring and other metadata of the input function
"""

import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Return a friendly greeting."""
    return 'Hello!'

print(greet.__name__)
# if you remove funtools.wraps the below output is None.
print(greet.__doc__)
"""
***Note:
Best practice always use functool.wraps in all of the decorators 
you write yourself.
"""
