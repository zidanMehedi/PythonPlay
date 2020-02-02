print('Enter An Integer Number To Reverse It...')
num=int(input('Enter Number: '))
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print('The Reverse Of The Given Number Is: ',rev)
