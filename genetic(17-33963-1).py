import random

x1=[9,8,7,6,5,4,3,2]
x2=[6,5,9,8,3,2,5,4]
x3=[3,2,5,4,7,6,9,8]
x4=[2,1,6,5,7,6,5,4]

def fitness(crmsm):
    return ((crmsm[0]-crmsm[1])+(crmsm[2]-crmsm[3])+(crmsm[4]-crmsm[5])+(crmsm[6]-crmsm[7]))

def totalFitness():
    return(fitness(x1)+fitness(x2)+fitness(x3)+fitness(x4))

def totalSample():
    return len([x1,x2,x3,x4])

def average():
    return (totalFitness()/totalSample())



def probability(crmsm):
    return (crmsm/totalFitness())

def expectedCount(crmsm):
    return (probability(crmsm)*totalSample())

def associatedBin(end,start=0.0):
    stop=start+end
    return stop
    
##def cross(P1,P2):
    

print("Fitness value for X1 : ",fitness(x1))
print("Fitness value for X2 : ",fitness(x2))
print("Fitness value for X3 : ",fitness(x3))
print("Fitness value for X4 : ",fitness(x4))
print()
print('Average : ',average())
print('Total Sample: ',totalSample())

print('Total Fitness: ',totalFitness())
print()
print("Probability for X1 : ",probability(fitness(x1)))
print("Probability for X2 : ",probability(fitness(x2)))
print("Probability for X3 : ",probability(fitness(x3)))
print("Probability for X4 : ",probability(fitness(x4)))

print("Expected Count for X1 : ",expectedCount(fitness(x1)))
print("Expected Count for X2 : ",expectedCount(fitness(x2)))
print("Expected Count for X3 : ",expectedCount(fitness(x3)))
print("Expected Count for X4 : ",expectedCount(fitness(x4)))

XA1=0.0+associatedBin(probability(fitness(x1)))
XA2=XA1+associatedBin(probability(fitness(x1)))
XA3=XA2+associatedBin(probability(fitness(x2)))
XA4=XA3+associatedBin(probability(fitness(x3)))

list={
    'X1': [0.0,XA1],
    'X2': [XA1,XA2],
    'X3': [XA2,XA3],
    'X4': [XA3,XA4]
    }

##associatedBin(probability(fitness(x1)))

##print(list)
rand=[(round(random.uniform(0,1),2)),(round(random.uniform(0,1),2)),(round(random.uniform(0,1),2)),(round(random.uniform(0,1),2))]
##print(rand)

selection=[]

for x in range(4):
    if(list['X1'][0]<rand[x]<list['X1'][1]):
        selection.append(x1)
    if(list['X2'][0]<rand[x]<list['X2'][1]):
        selection.append(x2)
    if(list['X3'][0]<rand[x]<list['X3'][1]):
        selection.append(x3)
    if(list['X4'][0]<rand[x]<list['X4'][1]):
        selection.append(x4)
print()    
print('Selection=>',selection)


