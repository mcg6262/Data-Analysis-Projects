import numpy as np

list = [0,1,2,3,4,5,6,7,8]

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain 9 numbers.")
    print(list)
    
    array = np.array(list).reshape((3, 3))
    print(array)
    print(array.mean(0), array.mean(1), array.mean())

    cal = dict()
    cal['mean'] = [array.mean(0).tolist(), array.mean(1).tolist(), array.mean().tolist()]
    cal['variance'] = [array.var(0).tolist(), array.var(1).tolist(), array.var().tolist()]
    cal['standard deviation'] = [array.std(0).tolist(), array.std(1).tolist(), array.std().tolist()]
    cal['max'] = [array.max(0).tolist(), array.max(1).tolist(), array.max().tolist()]
    cal['min'] = [array.min(0).tolist(), array.min(1).tolist(), array.min().tolist()]
    cal['sum'] = [array.sum(0).tolist(), array.sum(1).tolist(), array.sum().tolist()]
    return cal
    
print(calculate(list))