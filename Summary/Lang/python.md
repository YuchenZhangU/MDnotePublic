
## Meta

```python
# check current version
import sys
print(sys.version)
```

## Data Type

### String

```python
# Literal String Interpolation (f-strings)
# only for python version > 3.6
    
```

## Functional Programing

General Form:
`function_name(function_to_apply, iterable_of_elements)`

sorted
map
filter
reduce

```python
# Partial function
from functools import partial

def add(a, b):
    return a + b


add_two = partial(add, 2)
```

## Loop

```python
l = [1,2,3,4,5]
for i in l:
    print(i)

# print 0 - 9
for i in range(10):
    print(i)

# print 1, a ...
d = ['a','b', 'c', 'd', 'e']
for i,j in zip(l,d):
    print(i, j)

# print 0, a ...
for i,j in enumerate(d):
    print(i,j)


dic = {'a': 'guauga', 'b': 'jaijia'}
for k,v in dic.iteritems():
    print(k,v)

```