# Polymorphism

# One name but multiple forms/behaviours is called polymorphism

# Overloading:
# a) Method overloading (Not supported)
# b) Constructor overloading (Not supported)
# c) Operator overloading

# Overriding:
# a) Method overriding (last defined method will executed)
# b) constructor overriding (last defined constructor will executed)


# Operator overloading:

# +  ===> is used to adding and concatenating, 

# 1+1 = 2
# "a" + "b" = "ab"

# Method overriding: (Inheritance Example)

class P:
    def property(self):
        print("cash")

    def marry(self):
        print('yankayamma')

class C(P):
    def marry(self):
        super().marry()
        print('katrina')

c = C()
c.marry() # katrina
c.property() # cash

# Constructor overriding:

class P:
    def __init__(self):
        print("this is first constructor")

    def __init__(self):
        print("this is second constructor")

p = P() # print this is second constructor.
