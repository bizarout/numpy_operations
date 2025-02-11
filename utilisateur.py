from dataclasses import dataclass, field

@dataclass(frozen=True)
class Person:
    name:str
    age:int
    hobbies:list = field(default_factory=list)
    


def my_decorator(func):
    import numpy as np 
    def wrapper(*args,**kwargs):
        print("before")
        func(*args, **kwargs)
        print("after function")
        
    return wrapper
        

@my_decorator 
def produitSclaire(v1,v2):
    import numpy as np 
    v3 = np.dot(v1,v2)
    
    return v3
    
    
    
print(produitSclaire([3,4],[4,9]))

