print('1.Rock')
print('2.Paper')
print('3.Scissors')
print()
num=int(input('Select an Option: '))

if num==1:
	print('You Have Chosen Rock!')
elif num==2:
	print('You Have Chosen Paper!')
elif num==3:
	print('You Have Chosen Scissors!')
else:
	print('Invalid Option!')

import random
import time
print()
print("Wait For Opponet's Option")
time.sleep(1)
com=random.randint(1,3)
print()
if com==1:
	print('Opponent Has Chosen Rock!')
elif com==2:
	print('Opponent Has Chosen Paper!')
elif com==3:
	print('Opponent Has Chosen Scissors!')
print()
print('Wait For The Result')
time.sleep(0.5)
print()
if com==num:
	print('Draw!')
elif num==1 and com==2:
	print('You Lose!')
elif num==1 and com==3:
	print('You Win!')
elif num==2 and com==1:
	print('You Win!')
elif num==2 and com==3:
	print('You Lose!')
elif num==3 and com==1:
	print('You Lose!')
elif num==3 and com==2:
	print('You Win!')
else:
	print('Invalid Operation')
