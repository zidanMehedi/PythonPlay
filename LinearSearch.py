def linearSearch(A):
    x=int(input('Enter A Number To Search : '))
    for i in range(len(A)):
        if A[i]==x:
            index=A.index(A[i])
            break
        elif A[i]!=x:
            index=-1
    if(index==-1):
        print('{0} has not been found'.format(x))
    else:
        print('{0} has been found in index {1}'.format(x,index))
A=[2,4,1,9,7,8,5]
linearSearch(A)
