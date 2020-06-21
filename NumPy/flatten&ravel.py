import numpy as np

###This flatten method, converts multi-dimensional array to 1D array. This is not a NumPy method###

arr = np.random.rand(5,3)
print(arr.flatten()) #return 1D array in C style
print(arr.flatten('F')) #return 1D array in Fortran style

arr = np.array([[[1,2,3,4,5],[5,4,3,2,1]],[[6,7,8,9,10],[10,9,8,7,6]]])
print(arr.flatten()) #returns 1D array in C style
print(arr.flatten('F')) #returns 1D array in Fortran style

###ravel function works like flatten but ravel in a NumPy method

arr = np.random.rand(5,3)
print(arr.ravel()) #returns 1D array in C style
print(arr.ravel('F')) #returns 1D array in Fortran style
print()
print(np.ravel(arr)) #returns 1D array in C style
print(np.ravel(arr,order='F')) #return 1D array in Fortran style

arr = np.array([[[1,2,3,4,5],[5,4,3,2,1]],[[6,7,8,9,10],[10,9,8,7,6]]])
print(np.ravel(arr)) #returns 1D array in C style
print(np.ravel(arr,order='F')) #returns 1D array in Fortran style
print()


