import datetime
import time

date = datetime.datetime.now()

print(date.strftime('%B'))
print(date.strftime('%a').upper())
print(date.strftime('%T'))
time.sleep(2)
print(date.strftime('%H:%M:%S')) #sleep method doesn't affect the second/time
print(date.strftime('%d-%m-%Y'))
print(date.strftime('%D'))
print(date.strftime('%d %B,%Y %A'))
