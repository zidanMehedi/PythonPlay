a=int(input('Enter 1st Number: '))
b=int(input('Enter 2nd Number: '))
c=int(input('Enter 3rd Number: '))
if a>b:
    if a>c:
        print('a is {0} and Largest of all numbers'.format(a))
    else:
        print('c is {0} and Largest of all numbers'.format(c))
elif b>c:
    print('b is {0} and Largest of all numbers'.format(b))
elif a==b==c:
    print('All numbers are Equal')
else:
    print('c is {0} and Largest of all numbers'.format(c))

if a<b:
    if a<c:
        print('a is {0} and Smallest of all numbers'.format(a))
    else:
        print('c is {0} and Smallest of all numbers'.format(c))
elif b<c:
    print('b is {0} and Smallest of all numbers'.format(b))
else:
    print('c is {0} and Smallest of all numbers'.format(c))
