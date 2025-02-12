from dataclasses import dataclass, field

@dataclass(frozen=True)
class Person:
    name:str
    age:int
    hobbies:list = field(default_factory=list)
    


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
