import numpy as np
x_k = []


def jacobi(A, x_0,b):
    for i in range(3):
        (1/A[i][i])*


#Initial values
As = np.array([[5,1,2],[-1,4,-1], [-2,6,10]])
x_0s = np.array([[0],[0],[0]])
b = np.array([[1],[1],[1]])

test = jacobi(As, x_0s,b)

