def binarySearch(A):
    x=int(input('Enter A Number To Search : '))
    A.sort()
    low=1
    high=len(A)
    for i in range(len(A)):
        mid=int(low+((high-low)/2))
        if(A[mid]==x):
            print('{0} Found'.format(x))
            break
        elif(A[mid]<x):
            low=mid+1
        elif(A[mid]>x):
            high=mid-1
        else:
            print('{0} Not Found'.format(x))
            break
A=[2,5,4,6,1,0,99]
binarySearch(A)
