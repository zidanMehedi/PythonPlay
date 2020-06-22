import numpy as np

mat = np.matrix('1 2;3 4')
matpow = np.linalg.matrix_power(mat,2) #returns (mat*mat)
print(matpow)
print(mat*mat)
print(mat.dot(mat))
print()

mat = np.matrix('1 2 3;4 5 6;7 8 9')
matinv = np.linalg.inv(mat)
matpow = np.linalg.matrix_power(mat,-1)
print(matpow)
print(matinv)


mat = np.matrix('1 2 3 4;4 5 6 8;7 8 9 10;13 14 15 16')
matinv = np.linalg.inv(mat)
matpow = np.linalg.matrix_power(mat,-1) #returns inverse of mat
print(matpow)
print(matinv)

mat = np.matrix('1 2;4 5')
matpow = np.linalg.matrix_power(mat,-2) #at first does (mat*mat) and then returns inverse of (mat*mat)
print(matpow)
print()


mat = np.matrix('1 2;3 4')
matpow = np.linalg.matrix_power(mat,0) #returns identity matrix
print(matpow)

mat = np.matrix('1 2 3 4;4 5 6 8;7 8 9 10;13 14 15 16')
matpow = np.linalg.matrix_power(mat,0) #returns identity matrix
print(matpow)
