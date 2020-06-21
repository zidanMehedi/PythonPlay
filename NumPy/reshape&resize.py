import numpy as np


###In reshape method, the new shape must follow row * column = size of array###

arr = np.arange(1,11)
print(np.reshape(arr,(5,2))) #returns new shaped array

print(np.reshape(arr,(5,2),order='F')) #returns new shaped array in Fortran style

print(arr.reshape((2,5))) #another way of reshape

###In resize method, new shape doesn't matter on size of array. If the size of array doesn't match, it will repeat the elements again###

print(np.resize(arr,(5,4)))