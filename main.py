import numpy as np 
from utilisateur import Person

def operations(v1,v2,oprs):
    if oprs =="+":
        if v1.shape==v2.shape:
            return v1 + v2
        else:
            print(" erreur de taille des matrices ")
    if oprs == "-":
        return v1-v2
    if oprs ==".":
        return np.dot(v1,v2)

v1 = np.array([[1,2],[2,4]])
v2 = np.array([1,3])
print(operations(v1,v2,"-"))

p1 = Person("hamid",33," internet , data ...")

print(p1.nameMethod)

    