import numpy as np

###insert###

#rules: to add data in 1D array, just say the position before where the data will be inserted, axis will be by default none. For data insertion in 2D array,
#if a single value is added, the array will be flattered first and insert the data before the mentioned position. To insert a set of data vertically, the number
#of elements in the list must be equal to the number of columns of the array and the axis will be 0. On the otherhand, To insert a set of data horizontally,
#the number of elements in the list must be equal to the number of rows of the array and the axis will be 1. For different data type value inertion,
#the new value is autometically casted to array data type

arr = np.arange(10)
print(np.insert(arr,3,25))
print(np.insert(arr,3,[25,26,27]))
print(np.insert(arr,(3,5),25)) #insertion of data before multiple positions
print(np.insert(arr,(3,5),[25,26])) #insertion of multiple data before multiple positions accordingly

arr = np.arange(1,21).reshape(4,5)
print(arr)
print(np.insert(arr,4,30))
print(np.insert(arr,3,30,axis=0)) #insertion of single value vertically
print(np.insert(arr,4,30,axis=1)) ##insertion of single value horizontally
print(np.insert(arr,3,[30,31,32,33,34],axis=0))#insertion of multiple value vertically, column same
print(np.insert(arr,4,[30,31,32,33],axis=1)) #insertion of multiple value horizontally, row same
print()

###append###

#does almost same job like insert method but inserts new data at last position, so position doesn't need to be declared.


arr = np.arange(10)
print(np.append(arr,25))
print(np.append(arr,[25,26,27]))

arr = np.arange(1,21).reshape(4,5)
print(arr)
print(np.append(arr,30))
print(np.append(arr,[[30,31,32,33,34]],axis=0))#insertion of multiple value vertically, here the array of new values dimension must
                                               #follow the same dimension of array, column same
print(np.append(arr,[[30],[31],[32],[33]],axis=1)) #insertion of multiple value horizontally, here the array of new values dimension must
                                                   #follow the same dimension of array, row same


###delete###

#rules: to remove data from array, just say the array itself and the removal data position. In case of 1D array, the axis will be none. In case of multi-dimensional
#array, if axis is none, then the array will be flattered and the value will be deleted. To remove a set of the from a vertical position, say the position and keep
#axis as 0. On the otherhand, to remove a set of the from a horizontal position, say the position and keep axis as 1.

arr = np.arange(10)
print(np.delete(arr,5)) #removing a single value
print(np.delete(arr,(1,4,6))) #removing multiple values

arr = np.arange(1,21).reshape(4,5)
print(arr)
print(np.delete(arr,5)) #flattered for not calling axis in 2D array
print(np.delete(arr,2,axis=0)) #removed dataset of 3rd vertical row
print(np.delete(arr,4,axis=1)) #removed dataset of 5th horizontal column
