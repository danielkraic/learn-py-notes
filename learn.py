#!/usr/bin/python

# http://www.afterhoursprogramming.com/tutorial/Python/
# https://docs.python.org/3.4/tutorial/index.html

print('hello')
print('hello\nhello2')
print(r'1\n2')
print('%.2f' % 10)
print('%.5s' % 'abcdefgh')

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('a {0} b {1}'.format(10, 11))
print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('{0:10} -> {1:5}'.format('a', 'b'))

#'!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))

#comment
'''
commented
'''

#values
a=2
b="2"
c=1.1
x,y = 1,10

a=0b1
a=0x1
a=1+3j

a,b,c=1,2,'g'
x=y=z=0

del x

int(b)
float(b)
complex(1,3)
str(c)

str1="""very
log
string"""
str2='''very
log
string'''
print('''\
Usage:
  -h help
  -f force\
''')
print('a' 'b'
'c')

type(a)
type(1.1)

ord('c') # 99
chr(99)  # 'c'

hex(16)
oct(16)

#operators
+ - * / % ** // floor division

# conditions
if 1 > 2:
    print(1)
elif 1 == 2:
    print(2)
else:
    print(3

A and B and C
A or B or C
A and (not B) or C

#func
def myfunc(val1, val2=True):
    '''simple func

    Returns: string
    '''
    return 'hello' + str(val1) + str(val2)

print(myfunc())

#loops
for a in range(1,10):
    print(a)
for a in reversed(range(1,10, 2)):
    print(a)
for a in sorted(set('abracadabra')):
    print(a)

a=0
while a < 10:
    print(a)
    a+=1

# strings
'abcd'.count('a')
'abcd'.find('a') # position or -1
'ABC'.lower()
'abc'.upper()
'a'.center(3)
'a'.rjust(3)
'1'.zfill(3)
' abc '.strip()
'abc'.replace('a', 'x')
'abc'.capitalize()
'abc'.isdigit()
'abc'.islower()
'a;b;c'.split(';')
'a\nb\nc'.splitlines()

'abcd'[2]
'abcd'[1:3]
'abcd'[1:-2]
'abcd'[2:]
'abcd'[:3]
'abcd'[-3:-1]

#lists
arr=[1,2,3]
arr += [4,5,6]
arr[1]
squares = [x**2 for x in range(10)]

for v in arr:
    print(v)

for i in range(len(arr)):
    print(i, arr[i])

for i in range(10):
    print(i, arr[i])

for i in range(5,20,5):
    print(i, arr[i])

if 2 in arr:
    print('y')

if 2 not in arr:
    print('n')

arr.append(10)
arr.extend([10,11,12])

arr.count(3)
arr.index(5)
arr.insert(position, value)
arr.remove(2)
v = arr.pop()
arr.sort()
arr.reverse()

arr[2:-1]=[1,2,3]
arr[2:-1]=[]
del a[3]
del a[4:]
len(a)
max(a)
min(a)

[1,2,3] + [4,5,6]
[1,2,3] * 2

list(enumerate(list('abc'))
list(enumerate(list('abc'), start=1)
for i, v in enumerate(['a', 'b', 'c']):
    print(i, v)

a1=[1,2,3,4]
a2=['a', 'b', 'c', 'd']
for x, y in zip(a1, a2):
    print(x, y)

#tuples
t=(1,2,3)
t2=()
t3=(2,)
mylist=list(t)

#sets
st={1,2,3,1,5,3,7}
a=set('abracadabra')
s={x for x in 'abracadabra' if x not in 'abc'}
s1 - s2
s1 | s2
s1 & s2
s1 ^ s2

#dict
d={'val1': 11, 'val2': 12}
d['val1'] = 10
for i in d:
    print(i, d[i])
for k,v in d.items():
    print(k, v)

#exceptions
raise NameError('HiThere')

try:
    print('v'+3)
except:
    print('oh')

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print('file ok...')
    f.close()

#output
str(obj)
repr(obj)

#files
f=open('file.txt', 'r')
f.close()

f.read(1)
f.readline()
f.read()

li=[]
for line in f:
    li.append(line)

f=open('test.txt', 'w')
f.write('1')
f.write('line\n')
f.close()

f=open('test.txt', 'a')
f.write('line\n')
f.close()

#classes
class Pr:
    def __init__(self):
        self.val=0
    def get(self):
        return self.val
    def set(self,v):
        self.val=v

a=Pr()
a.get()
a.set(12)

# modules
import mymodule
from mymodule import fnc1, fnc2
from mymodule import *

import path.to.mymodule
from path.to.mymodule import myfunc

import sys
dir(mymodule)

dir() # list all defined names

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

#sys
sys.argv
sys.stdout
sys.srderr.write('err1')

#os
os.getcwd()
os.chdir('/etc')
os.system('mkdir alsa')
dir(os)
help(os)

#shutil
shutil.move('f1', 'f2')

#glob
glob.glob('*.py')

#re
re.findall()
re.sub()

#math
math.cos(math.pi/4)

#random
random.random()
random.choice(['a', 'b', 'c'])

#datetime
#time
import time
time.time()
time.ctime()
time.asctime(time.localtime(time.time()))
time.sleep(1) #1s

#calendar
import calendar
print(calendar.month(2015, 11))

#queue
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
