import numpy as np

A = np.array([[8,0, 12], [1,-2,1],[0,3,0]])
x_0 = np.array([[1], [0], [0]])
x_k = x_0
alfa = -1.4
for i in range(5):
    y_k = np.matmul(np.linalg.inv(A-alfa*np.identity(3)),x_k)
    u_k = np.max(y_k)
    v_k = alfa + 1/u_k
    x_k_1 = (1/u_k)*y_k
    print("%.4f" % v_k)
    x_k = x_k_1

    