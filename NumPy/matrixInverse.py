import numpy as np

mat = np.matrix('1 2;5 6')
matinv = np.linalg.inv(mat) #return inverse of matrix
print(matinv)
print(np.allclose(mat.dot(matinv),np.eye(2)))
print()


##mat = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
##matinv = np.linalg.inv(mat)
##print('This is original matrix:\n',mat)
##print()
##print('This is inverse matrix:\n',matinv)
##print('This is the dot product of matrix and inverse matrix:\n',mat.dot(matinv))
