import numpy as np

arr = np.array([1,2,3,4,5]) #simple array
print(arr)
print()

list = [10,20,30]
arr = np.array(list) #putting list inside array function
print(arr)
print()

arr = np.array(list, dtype='f') #specified data type, here 'f' means float
print(arr)
print()

arr = np.array(list,'complex') #specified data type, dtype is assigned according to parameter position
print(arr)
print()

arr = np.array([[1,2,3],[4,5,6]]) #2D array
print(arr)
print()

arr = np.array([[[1,2,3],[4,5,6]],[[10,20,30],[40,50,60]]]) #3D array, more clearly array of arrays
print(arr)
print()


arr = np.arange(1,10) #this function creates an array from start to (end-1) by default
print(arr)
print()

arr = np.arange(1,10,2) #third paraeter refers to step towards next value.
print(arr)
print()

arr = np.arange(1,100,10) #third paraeter refers to step towards next value.
print(arr)
print()

arr = np.arange(10,100,10) #third paraeter refers to step towards next value.
print(arr)
print()

arr = np.arange(10) #this parameter refers to the end point only
print(arr)
print()

arr = np.arange(5.0) #this parameter refers to the end point only
print(arr)
print()

arr = np.arange(10,100,10,dtype='complex') #it will generate complex values
print(arr)
print()

zero = np.zeros(5) #creates 1D array of zeros
print(zero)
print()

zero = np.zeros(5,dtype=int) #creates 1D array of zeros and datatype integer
print(zero)
print()

zero = np.zeros((5,3),dtype=int) #creates 2D array of zeros and datatype integer
print(zero)
print()

one = np.ones(5) #creates 1D array of ones
print(one)
print()

one = np.ones(5,dtype=int) #creates 1D array of ones and datatype integer
print(one)
print()

one = np.ones((5,3),dtype=int) #creates 2D array of ones and datatype integer
print(one)
print()

arr = np.linspace(2,3) #returns by default 50 sample of evenly distributed numbers from start to end
print(arr)
print()

arr = np.linspace(2,3,endpoint=False) #returns by default 50 sample of evenly distributed numbers from start to end, excludes endpoint
print(arr)
print()

arr = np.linspace(2,3,endpoint=False, retstep=True) #returns by default 50 sample of evenly distributed numbers from start to end, excludes endpoint, also returns setps
print(arr)
print()

arr = np.linspace(2,8,num=10) #returns 10 sample of evenly distributed numbers from start to end
print(arr)
print()

arr = np.linspace(2,16,num=12, dtype=int) #returns 12 sample of evenly distributed integer numbers from start to end
print(arr)
print()

eye = np.eye(3) #return identity alike array
print(eye)
print()

eye = np.eye(5,4) #return identity alike array but with different rows and columns
print(eye)
print()

eye = np.eye(3, k=1) #k referes position of 1's, 
print(eye)
print()

eye = np.eye(5, k=-1) #k referes position of 1's, 
print(eye)
print()

eye = np.eye(5, k=-2) #k referes position of 1's, 
print(eye)
print()

eye = np.eye(5, k=2) #k referes position of 1's, 
print(eye)
print()

eye = np.eye(5,dtype=int) #return identity alike array of integer values 
print(eye)
print()

iden = np.identity(5) #return exact identity array
print(iden)
print()

iden = np.identity(3,int) #return exact identity array of int values
print(iden)
print()



