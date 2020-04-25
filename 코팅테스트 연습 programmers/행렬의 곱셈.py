def solution(arr1, arr2):
    import numpy as np
    a=np.array(arr1)
    b=np.array(arr2)
    return np.matmul(a,b).tolist()

def sol(arr1,arr2):
    return list(zip(*arr2))
print(solution([[1, 4], [3, 2], [4, 1]],[[1, 2], [3, 4]]))
