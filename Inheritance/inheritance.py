# Inhertance types:
# ----------------

# 1. Single Inhertance
# 2. Multiple Inheritance (inherting more than one class at a time)
# 3. Multi level Inheritance (A -> B -> C -> D)
# 4. Hierarchy Inheritance (like tree and graph data structure)
# 5. Hybrid Inheritance


# single Inheritance:

class P:
    def m1(self):
        print('Parent method')

class C(P):
    def m2(self):
        print("Child method")

c = C()
c.m1()
c.m2()

# Multi Level inheritance

class P:
    def m1(self):
        print('Parent method')

class C(P):
    def m2(self):
        print("Child method")

class SubChild(C):
    def m3(self):
        print('sub child method')

c = SubChild()
c.m1()
c.m2()
c.m3()

# Multiple Inheritance

class P1:
    def m1(self):
        print('First Parent method')

class P2:
    def m1(self):
        print("Second parent method")

class C(P1,P2):
    def m1(self):
        print('child method')

c = C()
c.m1() # child method.

# Note:
# 1. order of parent inheritance is preserved
# 2. method execution is in the following order
#     a) child class first
#     b) P1 class second
#     c) P2 class third



# Hierarichal inheritance

class P:
    def m1(self):
        print('Parent method')

class C1(P):
    def m2(self):
        print(" first Child method")

class C2(P):
    def m3(self):
        print('Second child method')

c = C1()
c.m1()
c.m2()

x = C2()
x.m1()
x.m3()

# Hybrid inheritance

# Combination of inhertances is called Hybrid inheritance.
