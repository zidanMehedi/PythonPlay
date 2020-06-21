import numpy as np

#indexing

arr = np.array([1,2,3,4,5,6,7,8]) 
print(arr[2]) #returns specific value

arr = np.array([1,2,3,4,5,6,7,8]) 
print(arr[-3]) #returns specific value with negative indexing

arr = np.array([[1,2,3,4],[5,6,7,8],[10,20,30,40]])
print(arr[2]) #2D indexing

arr = np.array([[1,2,3,4],[5,6,7,8],[10,20,30,40]])
print(arr[1][3]) #2D indexing

arr = np.array([[[1,2,3,4],[5,6,7,8]],[[10,20,30,40],[50,60,70,80]]])
print(arr[0][1][0]) #3D indexing, [array] [row] [column]

arr = np.array([[[1,2,3,4],[5,6,7,8]],[[10,20,30,40],[50,60,70,80]]])
print(arr[1][0][1]) #3D indexing, [array] [row] [column]


#slicing

arr = np.array([1,2,3,4,5,6,7,8]) 
print(arr[2:5]) #returns sub-array

arr = np.array([1,2,3,4,5,6,7,8]) 
print(arr[2:]) #returns sub-array starts from index 2 ends in last index

arr = np.array([1,2,3,4,5,6,7,8]) 
print(arr[:6]) #returns sub-array starts from first index ends in index (6-1)

arr = np.array([1,2,3,4,5,6,7,8]) 
print(arr[2:7:2]) #returns sub-array from index 2 to index (7-1) excluding 2 steps

arr = np.array([1,2,3,4,5,6,7,8]) 
print(arr[::3]) #returns sub-array from index 1 to index (last-1) excluding 3 steps

arr = np.array([1,2,3,4,5,6,7,8]) 
print(arr[3::2]) #returns sub-array from index 3 to index (last-1) excluding 2 steps

arr = np.array([1,2,3,4,5,6,7,8]) 
print(arr[-7:-2]) #returns sub-array with negative index starting from (-2-1) to -7

arr = np.array([[1,2,3,4],[5,6,7,8],[10,20,30,40]])
print(arr[1:,2:]) #2D indexing

arr = np.array([[1,2,3,4],[5,6,7,8],[10,20,30,40]])
print(arr[0:2,1:]) #2D slicing

arr = np.array([[1,2,3,4],[5,6,7,8],[10,20,30,40],[50,60,70,80]])
print(arr[0:3,2:3]) #2D slicing

arr = np.array([[1,2,3,4],[5,6,7,8],[10,20,30,40],[50,60,70,80]])
print(arr[::2,1::2]) #2D slicing

#Advanced Indexing

arr = np.arange(5,100,5)
print(arr[[3,7,11]]) #returns only selected indexed values

arr = np.arange(5,100,5)
print(arr[[3,7,3,7,3,7,3,7]]) #returns only selected indexed values as much time as called

arr = np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11]])
print(arr)
print(arr[[1,2],[3,3]]) #returns only selected indexed values from 2D array

print(arr[[1,2,0],[3,3,1]]) #returns only selected indexed values from 2D array

print(arr[[1,2,1,2,1,2,1,2],[3,3,3,3,3,3,3,3]]) #returns only selected indexed values from 2D array as much time as called

arr = np.random.randn(5,3)
print(arr)
print(arr[arr>0]) #boolean indexing, returns all positive numbers of array

print(arr[arr<0]) #boolean indexing, returns all negative numbers of array












