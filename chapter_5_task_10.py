import numpy as np

# Numbers for task 5.8.10
A = np.array([[1,2,-2], [1,1,9], [0,1,9]])
x_0 = np.array([[1], [0], [0]])

x_k_list = []
u_k_list = []
x_k = x_0

for i in range(9):
    u_k = np.max(np.matmul(A,x_k))
    #print("x_k:",x_k,"  u_k:", u_k)
    x_k_list.append(x_k)
    x_k = (1/u_k)*(np.matmul(A,x_k))
    u_k_list.append(u_k)


print("u_k_5:",u_k_list[5],"    u_k_6:",u_k_list[6],"   x_k_5:", x_k_list[5],"  x_k_6:", x_k_list[6])

    