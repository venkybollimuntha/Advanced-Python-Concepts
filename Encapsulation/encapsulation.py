# Encapsulation prevents from accessing accidentally, but not intentionally.

# Encapsulation is idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data
# _a is called protected member
# __a is called private member


class Test:
    __a = 10
    def __init__(self):
        self.name = "venky"
        self.__age = 25
        self._salary = 60000

    def __first(self):
        return self.__age

    def second(self):
        return self.__first()

    @classmethod
    def hello(cls):
        return cls.__a

    

t = Test()
print(t._salary)
t._Test__a = 30
print(t.hello())

print(t._Test__age) # name mangling, you can check with dir(t)

print(t.second())


# Example 2

class Car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
# redcar.__updateSoftware()  # Not accessable from object
redcar._Car__updateSoftware() # We can intentionally access like this.


# Example 3
class Car:
    __maxspeed = 0
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    
    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private
redcar.drive()

#If you want to change the value of a private variable, a setter method is used.

class Car:

    __maxspeed = 0
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    
    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxSpeed(self,speed):
        self.__maxspeed = speed

redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320) # This method will set private value to latest one
redcar.drive()
