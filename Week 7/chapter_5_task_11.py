import numpy as np

# Numbers for task 5.8.11
A = np.array([[5,2], [2,2]])
x_0 = np.array([[1], [0]])
x_k = x_0

for i in range(5):
    u_k = np.max(np.matmul(A,x_k))
    R_x = (np.matmul(np.transpose(x_k),A@x_k))/np.matmul((np.transpose(x_k)),x_k)
    x_k = (1/u_k)*(np.matmul(A,x_k))
    print("Eigen:", R_x)

    
    



