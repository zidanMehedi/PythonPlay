import numpy as np

#Rule1: if dimension of 2 arrays are different, 1 of the array row must be 1,their column number must be equal


arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr2 = np.array([1,2,3,4,5])

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)
print(arr1**arr2)
print(arr1%arr2)
print()

print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.divide(arr1,arr2))
print(np.power(arr1,arr2))
print(np.mod(arr1,arr2))
print()


#Rule2: if dimension of 2 arrays are different, and their column are different, one of their column size must be 1 and one of their row must be 1

arr1 = np.array([[1],[2],[3]])
arr2 = np.array([1,2,3,4])
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)


