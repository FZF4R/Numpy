import numpy 
import random

n=random.randrange(10)
A=numpy.zeros(n)
for i in range(0,n):
    A[i]=random.randrange(10)
print("Mảng khởi tạo: ")
print(A)

def SoftMax(X) :
    X=numpy.exp(X)
    X=X/numpy.sum(X)
    return X 
print("Kết quả: ")
print(SoftMax(A))