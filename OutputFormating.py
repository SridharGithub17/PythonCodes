#!/usr/bin/evn python 
## Output formating examples
import math

print(f'Area of a squre is :  {math.pi: .3f}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name,id in table.items():
    print (f'{name:10} ==> {id:10d}')

print('We are the {0} and {1} of this ear'.format('man', 'woman'))

print('We are the {1} and {0} of this ear'.format('man', 'woman'))

for i in range(1,10):
    print('{0:2d} {1:3d} {2:4d}'.format(i,i*i,i*i*i))


year=2000
event="Happy Holidays"

TotalYears = 2000*5

print(f'Evens in the year {year} is {event}')

print (f'Total no of years are:  ' + repr(TotalYears))

