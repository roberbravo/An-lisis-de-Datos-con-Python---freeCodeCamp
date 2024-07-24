import numpy as np

def calculate(list):
    array = np.array(list)
    if(array.size == 9):
        matriz = array.reshape(3,3)
    else: raise ValueError("List must contain nine numbers.")
    
    calculations = {
        "mean" : [matriz.mean(axis=0).tolist(),matriz.mean(axis=1).tolist(),array.mean()],
        "variance" : [matriz.var(axis=0).tolist(),matriz.var(axis=1).tolist(),array.var()],
        "standard deviation" : [matriz.std(axis=0).tolist(),matriz.std(axis=1).tolist(),array.std()],
        "max" : [matriz.max(axis=0).tolist(),matriz.max(axis=1).tolist(),array.max()],
        "min" : [matriz.min(axis=0).tolist(),matriz.min(axis=1).tolist(),array.min()],
        "sum" : [matriz.sum(axis=0).tolist(),matriz.sum(axis=1).tolist(),array.sum()]
    }

    return calculations
