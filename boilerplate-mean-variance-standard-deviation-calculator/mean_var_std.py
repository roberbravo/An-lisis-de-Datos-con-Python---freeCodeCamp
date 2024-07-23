import numpy as np

def calculate(list):
    array = np.array(list)
    if(array.size == 9):
        matriz = array.reshape(3,3)
    else: raise ValueError("List must contain nine numbers.")
    
    calculations = {
        "mean" : [matriz.mean(axis=0),matriz.mean(axis=1),array.mean()],
        "variance" : [matriz.var(axis=0),matriz.var(axis=1),array.var()],
        "standard deviation" : [matriz.std(axis=0),matriz.std(axis=1),array.std()],
        "max" : [matriz.max(axis=0),matriz.max(axis=1),array.max()],
        "min" : [matriz.min(axis=0),matriz.min(axis=1),array.min()],
        "sum" : [matriz.sum(axis=0),matriz.sum(axis=1),array.sum()]
    }

    return calculations
