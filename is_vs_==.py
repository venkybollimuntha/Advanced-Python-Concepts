# is --> is used when to check reference objects i.e id(object)
# == --> is used to check the content is same or not 
a = [1,2,3]
b = a
print(a ==b)  # True
print(id(a) ==id(b)) # True # both ids are same referencing to same object
print(a is b) # True
c = list(a)  # Creating a new object copy of list a
print(a ==c) # True, because elements are same
print(id(a) ==id(c)) # False because # reference Ids are different.
print(a is c) # False


#Note: is operator internally check id of the object
