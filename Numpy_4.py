import numpy as np
A=np.array([0, 9, 7, 5, 10, 20, 35, 58, 10000])
def Average():
    n=A.shape[0]
    if (n!=0):
        T=0
        print(A)
        for i in A:
            T=T+i
        T=T/n
        for i in range(0,n):
            A[i]=T
Average()
print(A)