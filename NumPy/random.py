import numpy as np

arr = np.random.rand(5,4) #returns random uniformly distributed array values 0 to 1 of row = 5 column = 4
print(arr)
print()

arr = np.random.randn(4,3) #returns random normally distributed array of row = 4 column = 3
print(arr)
print()

arr = np.random.ranf(4) #returns random uniformly distributed float array values 0 to 1
print(arr)
print()

arr = np.random.randint(10,size=10) #returns random uniformly distributed integer array values upto (end-1) of total 10 numbers
print(arr)
print()

