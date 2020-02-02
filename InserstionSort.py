def insertionSort(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i
        while j>0 and A[j-1]>key:
            print('Swapping {0} with {1}'.format(A[j-1],key))
            A[j],A[j-1]=A[j-1],A[j]
            print(A)
            j=j-1
        A[j]=key
        
A=[3,2,7,5,4,6]
insertionSort(A)
