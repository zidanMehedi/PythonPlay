num=int(input('Enter a number: '))
fac=1
for i in range(1,(num+1)):
    fac=fac*i
print('Factorial of {0} is {1}'.format(num,fac))
