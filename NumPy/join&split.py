import numpy as np

###Concatenate Function Joins 2 arrays, but dimension must be same###
arr1 = np.arange(1,16,2)
arr2 = np.arange(2,17,2)
Arr1 = np.resize(arr1,(4,3))
Arr2 = np.resize(arr2,(3,4))
print(np.concatenate((Arr1,Arr2.T))) #if arrays needs to be joined vertically, number of columns must be same and axis should be 0
print()
print(np.concatenate((Arr1,Arr2.T),axis=1)) #if arrays needs to be joined horizontally, number of rows must be same and axis should be 1
print()

###hstack and vstack###

print(np.hstack((Arr1,Arr2.T))) #another way of horizontal join
print(np.vstack((Arr1,Arr2.T))) #another way of vertical join


###Split function splits an array in equal portions according to requirment, the requirment must be declared such that the array can be splitted equally###

arr = np.arange(20)
print(np.split(arr,4))

arr = np.arange(20).reshape(4,5)
print(np.split(arr,2)) #splits array vertically
#print(np.split(arr,2,axis=1)) ->it can't split horizontally in equal portion

print(np.split(arr,5,axis=1))
print()

###hsplit & vsplit###

print(np.hsplit(arr,5)) #another way of horizontal split
print(np.vsplit(arr,2)) #another way of vertical split
