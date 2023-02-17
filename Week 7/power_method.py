import numpy as np

def power_method(A, x0, N, printing=False):
    x=x0
    for _ in range(N):
        y=A.dot(x)
        mu=y[np.argmax(np.abs(y))]
        x=y/mu
        if(printing):
            print("mu=")
            print(mu)
            print("y=")
            print(y)
            print("x=")
            print(x)
            print("\n")
    return x, mu


A=np.array([[6,7], [8,5]])
x0 = np.array([1,0])

power_method(A, x0, 10)