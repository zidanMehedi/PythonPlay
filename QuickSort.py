def partitionSimulation(A,low,high):
    pivot=A[high]
    i=-1
    for j in range(high):
        if A[j]<=pivot:
            i=i+1
            print('Swapping {0} with {1}'.format(A[i],A[j]))
            A[i],A[j]=A[j],A[i]
            print('After Swap -------> ',A)
            print()
    A[i+1],A[high]=A[high],A[i+1]
    print('Pivot {0} is placed in correct position'.format(pivot))
    print('After Pivot Position -------> ',A)

def partition(A,low,high):
    pivot=A[high]
    i=-1
    for j in range(high):
        if A[j]<=pivot:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]=A[high],A[i+1]
    return (i+1)

def quickSort(A,low,high):
    if(low<high):
        x=partition(A,low,high)
        quickSort(A,low,x-1)
        quickSort(A,x+1,high)
##        print(A)

A=[1,9,2,7,5]
partitionSimulation(A,0,len(A)-1)
quickSort(A,0,len(A)-1)
print()
print('After final sort -------> ',A)
