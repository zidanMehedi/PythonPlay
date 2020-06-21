import numpy as np

###Transpose Function makes Transpose of an array###

arr = np.arange(1,21).reshape(5,4)
print(arr)
print(np.transpose(arr)) #returns a view of original array in (1,0) axes, here 0:4 and 1:5

print(arr.transpose()) #another way of transpose
print(arr.T) #another way of transpose
print()

###swapaxes Function swaps between row and column###

arr = np.arange(1,21).reshape(5,4)
print(arr)
print(np.swapaxes(arr,1,0)) #returns a view of original array in (1,0) axes, here 0:4 and 1:5


arr = np.arange(1,21).reshape(5,4)
print(arr)
print(arr.swapaxes(1,0)) #another way, returns a view of original array in (1,0) axes, here 0:4 and 1:5

arr = np.arange(1,41).reshape(2,5,4)
print(arr)
print()
print(np.swapaxes(arr,2,1))
print()
print(np.swapaxes(arr,0,1))
print()