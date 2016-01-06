#!/usr/bin/python

# http://www.afterhoursprogramming.com/tutorial/Python/
# https://docs.python.org/3.4/tutorial/index.html

help() # interactive help
help(sys)
help(list)
help(tuple)
help(dict)
help(set)

print(print.__doc__)
print(sys.__doc__)

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
'{0:.1f} {1}'.format(size, suffix)

#'!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before it is formatted:
print('The value of PI is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))

si_suffixes=['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
'1000{0[0]} = 1{0[1]}'.format(si_suffixes) # '1000KB = 1MB'

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
isinstance(1, int)
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

#bytes
b1=b'abcd\x65'
b1=b'\xff'
b1=b'abcd\x65'
ba=bytearray(ba)
ba[0]=101 # bytearray(b'ebcd')
s1=b1.decode('ascii')
b1=s1.encode('ascii')

#lists
arr = [1,2,3]
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
v = arr.pop()  # last item
v = arr.pop(0) # first item
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

[i*i for i in [1,2,3]]
[i for i in range(10) if i % 2 != 0]
[ (i, i*i) for i in range(10) ]

[os.path.realpath(i) for i in glob.glob('[A-Z]*')]
[f for f in glob.glob('*.py') if os.stat(f).st_size > 6000]


#tuples
t=(1,2,3)
t2=()
t3=(2,)
mylist=list(t)

v = (1, '2', 3.0)
(x, y, z) = v
(Mon, Tue, Wed, Thu, Fri, Sat, Sun) = range(7)

#sets
s=set()
s=set('abracadabra')
s={1,2,3,1,5,3,7}
s=set(range(5))
s={x for x in 'abracadabra' if x not in 'abc'}
s1 - s2
s1 | s2
s1 & s2
s1 ^ s2

s.add(2)
s1.update(s2) # merge
s1.update([1,2,3,1,2,3])
s1.update(range(5))
s1.discard(2) # ignore if 2 not exists
s1.remove(2)  # raise KeyError if 2 not exists
s1.pop()
s1.clear()

2 in s1

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.union(s2) #{1, 2, 3, 4, 5, 6, 7, 8}
s1.intersection(s2) #{4, 5}
s1.difference(s2) #{1, 2, 3}
s1.symmetric_difference(s2) #{1, 2, 3, 6, 7, 8}

{1,2}.issubset(s1) #true
s1.issubset({1,2}) #true

#dict
d={'val1': 11, 'val2': 12}
dict(sape=4139, guido=4127, jack=4098)
d['val1'] = 10
'val1' in d
d.keys()
for i in d:
    print(i, d[i])
for k,v in d.items():
    print(k, v)
    
{i: i*i for i in range(5)}
{f: os.stat(f).st_size for f in glob.glob('*.py')}

d={os.path.realpath(f): os.stat(f).st_size for f in glob.glob('*.txt') if os.stat(f).st_size != 0}
for k,v in d.items():
  print(k, " ", v)

{v,k for k,v in d.items()}

#exceptions
raise NameError('HiThere')
raise ValueError('number must be non-negative')

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

try:
  from lxml import etree
except ImportError:
  import xml.etree.ElementTree as etree

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
os.getcwd() # curr dir, pwd
os.chdir('/etc')
os.path.join('/etc', 'sysctl.conf')
(d, f) = os.path.split('/etc/sysctl.conf')
(n, e) = os.path.splitext('/etc/sysctl.conf')
os.expanduser('~')
os.path.join(os.expanduser('~'), 'code', 'python')
os.path.exists(p)
os.path.isdir(p)
os.path.getsize(p)
os.path.basename(p)
os.path.dirname(p)
metadata=os.stat('/etc/passwd') # metadata,st_size
os.getenv('PATH')
os.system('mkdir alsa')
dir(os)
help(os)

#glob
glob.glob('*.py')

#shutil
shutil.move('f1', 'f2')

#re
re.findall()
re.sub()

#math
math.pi
math.cos(math.pi/4)

#fractions
x = fractions.Fraction(1,3)
x *= 2
x = fractions.Fraction(6,4) # 3/2

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
