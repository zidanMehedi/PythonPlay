def selectionSort(A):
    print('The list is ',A)
    print()
    for i in range(len(A)-1):
        min_index=i
        for j in range((i+1),len(A)):
            if A[j]<A[min_index]:
                min_index=j
        if min_index>i:
            print('Swapping {0} with {1}'.format(A[i],A[min_index]))
            A[i],A[min_index]=A[min_index],A[i]
            print('After Swap -------> ',A)
            print()
A=[3,2,5,9,7,8,13,12,10,22,18,16,15,21,25,24]
selectionSort(A)
