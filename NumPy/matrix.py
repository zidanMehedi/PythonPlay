import numpy as np

#matrix is little bit different from regular array
#matrix is always 2D
#matrix operation is differetnt from regular array operation

mat1 = np.matrix('1 2;4 5')
print(mat1)

mat2 = np.matrix([[5,6,7],[1,2,3]])
print(mat2)

print(np.append(mat1,[[3],[6]],axis=1)+mat2) #matrix addition
print(mat1*mat2) #matrix multiplication
print(mat1.dot(mat2)) #another way of matrix multiplication

print(np.transpose(mat1))
print(np.transpose(mat2))
