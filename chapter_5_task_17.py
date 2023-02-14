import numpy as np

A = np.array([[10,-8, -4], [-8,13,4],[-4,5,4]])
x_0 = np.array([[1], [0], [0]])
x_k = x_0
alfa = 3.3
for i in range(3):
    y_k = np.matmul(np.linalg.inv(A-alfa*np.identity(3)),x_k)
    u_k = np.max(y_k)
    v_k = alfa + 1/u_k
    x_k_1 = (1/u_k)*y_k
    print("%.4f" % v_k)
    x_k = x_k_1

    