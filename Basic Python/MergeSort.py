def mergeSort(A):
    if(len(A)==1):
        return A
    left=A[:len(A)//2]
    right=A[len(A)//2:]

    left=mergeSort(left)
    print(left)
    right=mergeSort(right)
    print(right)
    
    return merge(left,right)

def merge(arrayA,arrayB):
    arrayC=[]
    while(len(arrayA)!=0 and len(arrayB)!=0):
        if (arrayA[0]>arrayB[0]):
            arrayC.append(arrayB[0])
            arrayB.remove(arrayB[0])
        else:
            arrayC.append(arrayA[0])
            arrayA.remove(arrayA[0])
    while(len(arrayA)!=0):
        arrayC.append(arrayA[0])
        arrayA.remove(arrayA[0])
    while(len(arrayB)!=0):
        arrayC.append(arrayB[0])
        arrayB.remove(arrayB[0])
    return arrayC

A=[2,5,4,3,1]
print(mergeSort(A))
