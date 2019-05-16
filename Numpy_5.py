import numpy as np 
n=int(input())
A=-1*np.ones(n)
B=2*np.arange(int((n+1)/2))
A[B]=2-B*(0.25)
print(A)