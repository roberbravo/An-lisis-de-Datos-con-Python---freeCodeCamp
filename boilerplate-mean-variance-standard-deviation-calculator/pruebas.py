import numpy as np
def main():
    array = np.array([0,1,2,3,4,5,6,7,8])
    if(array.size == 9):
        matriz = array.reshape(3,3)
    else: raise ValueError("La lista debe contener nueve números")

    calculations = {
        'mean' : [matriz.mean(axis=0),matriz.mean(axis=1),array.mean()],
        'variance' : [matriz.var(axis=0),matriz.var(axis=1),array.var()],
        'standard deviation' : [matriz.std(axis=0),matriz.std(axis=1),array.std()],
        'max' : [matriz.max(axis=0),matriz.max(axis=1),array.max()],
        'min' : [matriz.min(axis=0),matriz.min(axis=1),array.min()],
        'sum' : [matriz.sum(axis=0),matriz.sum(axis=1),array.sum()]
    }

    print(calculations)



if __name__ == "__main__":
    main()