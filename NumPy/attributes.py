import numpy as np

#ndim

arr = np.array([1,2,3,4])
print(np.ndim(arr)) #returns dimension of array

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(np.ndim(arr)) #returns dimension of array

arr = np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
print(np.ndim(arr)) #returns dimension of array

#another way of ndim

print(arr.ndim) #returns dimension of array

#shape

arr = np.array([1,2,3,4])
print(arr.shape) #returns shape of array

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape) #returns shape of array

#another way of shape
print(np.shape(arr)) #returns shape of array

#size

arr = np.array([1,2,3,4])
print(arr.size) #returns number of elements in array

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.size) #returns number of elements in array

#another way of size
print(np.size(arr)) #returns number of elements in array

#dtype

arr = np.array([1,2,3,4])
print(arr.dtype) #returns dtype

arr = np.array([[1,2,3,4],[5.0,6.0,7.0,8.0]])
print(arr.dtype) #returns dtype


#itemsize

arr = np.array([1,2,3,4])
print(arr.itemsize) #returns itemsize

arr = np.array([[1,2,3,4],[5.0,6.0,7.0,8.0]])
print(arr.itemsize) #returns itemsize

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.itemsize) #returns itemsize


