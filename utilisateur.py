from dataclasses import dataclass, field

# @dataclass(frozen=True)
class Person:
    def __init__(self,name:str,age:int,hobbies:list ):
        self._name = name
        self._age = age
        self._hobbies = hobbies
    
    @property
    def nameMethod(self):
        return self._name
    
    def setName(self,name):
        self._name = name


def my_decorator(func):
    def wrapper(*args):
        print("before")
        func(*args)
        print("after function")
        
    return wrapper
        

@my_decorator 
def produitSclaire(v1,v2):
    import numpy as np 
    v3 = np.dot(v1,v2)
    print(v3)
    
    return v3
    
    
import numpy as np     
v = produitSclaire(np.array([3,4]),np.array([4,9]))

print(v)


p1 = Person("hamid",33," internet , data ...")

p1.setName("Ahmed")

print(p1.nameMethod)
