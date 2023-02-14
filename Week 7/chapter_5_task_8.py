import numpy as np

# Numbers for task 5.8.8
A = np.array([[2,1], [4,5]])
x_0 = np.array([[1], [0]])

x_k_list = []
u_k_list = []
x_k = x_0

for i in range(5):
    u_k = np.max(np.matmul(A,x_k))
    #print("x_k:",x_k,"  u_k:", u_k)
    x_k_list.append(x_k)
    x_k = (1/u_k)*(np.matmul(A,x_k))
    u_k_list.append(u_k)


print(x_k_list)


    