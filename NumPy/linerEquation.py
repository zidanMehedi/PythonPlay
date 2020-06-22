import numpy as np

#3x + y = 9
#x + 2y = 8

arrA = np.array([[3,1],[1,2]])
arrB = np.array([9,8])
result = np.linalg.solve(arrA,arrB) #returns the solution of linear equations
print('3x + y = 9')
print('x + 2y = 8')
print()
print(result)
print('x : {0}\t y : {1}'.format(result[0],result[1]))
print()


#6x + 2y - 5z = 13
#3x + 3y - 2z = 13
#7x + 5y - 3z = 26

arrA = np.array([[6,2,-5],[3,3,-2],[7,5,-3]])
arrB = np.array([13,13,26])
result = np.linalg.solve(arrA,arrB) #returns the solution of linear equations
print('6x + 2y - 5z = 13')
print('3x + 3y - 2z = 13')
print('7x + 5y - 3z = 26')
print()
print(result)
print('x : {0}, y : {1}, z : {2}'.format(round(result[0]),round(result[1]),round(result[2])))
