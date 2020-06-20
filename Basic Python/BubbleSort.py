def bubbleSort(A):
    print('The list is ',A)
    print()
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                print('Swapping {0} with {1}'.format(A[j],A[j+1]))
                A[j],A[j+1]=A[j+1],A[j]
                print('After Swap -------> ',A)
                print()

A=[3,2,6,4,9,7,1,5]
bubbleSort(A)
