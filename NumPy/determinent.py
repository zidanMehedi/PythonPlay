import numpy as np

mat = np.matrix('1 2;3 4')
matdet = np.linalg.det(mat) #returns determinent ((1*4)-(2*3))
print(round(matdet))
print()
arr = np.array([[1,2],[3,4]])
arrdet = np.linalg.det(arr) #returns determinent ((1*4)-(2*3))
print(round(arrdet))
print()
mat = np.matrix('1 2 3;4 5 6;7 8 9')
matdet = np.linalg.det(mat) #returns determinent (1*((5*9)-(6*8))-2*((4*9)-(6*7))+3*((3*4)-(5*7)))
print(round(matdet))
print()
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arrdet = np.linalg.det(arr) #returns determinent (1*((5*9)-(6*8))-2*((4*9)-(6*7))+3*((3*4)-(5*7)))
print(round(matdet))

