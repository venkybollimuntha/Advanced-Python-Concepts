#List, set, dict comprehensions:


[i for i in range(10) if i%2==0] # list comprehension

# [0,2,4,6,8]
{i for i in range(10) if i%2==0} # set comprehension
# [0,2,4,6,8]

name = ['venky','rakesh','yash','harish']
age = [25,24,26,26]

{name:age for name,age in zip(name,age)} # Dict comprehension

# {'venky': 25, 'rakesh': 24, 'yash': 26, 'harish': 26}

# there is no tuple comprehension, Because it internally generates generator object in python.
