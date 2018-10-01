# data structures

## build-in data structures

* container sequences: list, tuple, collections.deque (can hold items of different types)
* flat sequences: str, bytes, bytearray, memoryview, array.array - can hold items of one type


* mutable sequences: list, bytearray, array.array, collections.deque, memoryview
* immutable sequences: tuple, str, bytes

## list

```python
s + s2      # s.__add__(s2)
s += s2     # s.__iadd__(s2)
s.append(e)
s.extend(it)
s.clear()
s.insert(p, e)
s.pop()
s.remove(e)

e in s      # s.__contains__(e)
s.count(e)
s.index(e)
s[p]        # s.__getitem__(p)
s[p]        # s.__setitem__(p, e)

s.sort()
s.reverse()

s.copy()

s.__iter__()
len(s)      # s.__len__()
s * n       # s.__mul__(n)
s *= n      # s.__imul__(n)
n *= s      # s.__rmul__(n)

```

## tuple

### tuple unpacking

```python
a, b, *rest = range(10)
a, b, *rest, c, d = range(10)

func1(10, 0)
params = (20, 0)
func1(*params)

_, error = func3()

city_list = [
    ('Tokyo', 'Japan', 1900, (36.5, 42.1))
]
for city, state, year, (lang, long) in city_list
    pass
```

### named tuples

```python
from collections import namedtuple
Data = namedtuple('Data', 'a b c')
d1 = Data(1, 2, 3)
d2 = Data(a=1, b=2, c=3)

d1.a
d1._asdict()
d1._fields
Data._make([1,2,4])
```

### slices

```python
s[:]
s[2:]
s[:2]

s[::2]
s[::-1]
s[::-2]

del s[5:7]

s[2:5] = [10, 20]
s[2:5] = [100]
s[2:5] = []

s += [2, 3]
s *= 2
```

```python
s = [['_'] * 3] * 3 # wrong: will create 3 refs to same list
s = [['_'] * 3 for _ in range(3)]
s[1][2] = 'X'
```

### sorting

```python
s = "grape orange kiwi apple banana".split()

# create new list
sorted(s)
sorted(s, reverse=True)
sorted(s, key=len)
sorted(s, key=lambda x: x.lower(), reverse=True)

# sort list in place
s.sort(key=len, reverse=True)
```

### bisect - for sorted sequences

* binary search algorithm to find and insert items in sorted sequence

```python
import bisect
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]
```

```python
import bisect
s = list(range(0, 25, 5))
bisect.insort(s, 30)
```

### array

```python
from array import array
from random import random

a = array('d', [random() for _ in range(10)])
f = open('a1.txt', 'wb')
a.tofile(f)
f.close()

a2 = array('d')
f2 = open('a1.txt', 'rb')
a2.fromfile(f2, 10)
f2.close()
```