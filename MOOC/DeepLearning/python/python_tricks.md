## numpy

### basic

**Create a np array from list**

```python
# a vector
np.array([1,2,3])

# a matrix
np.array[([1,2,3],[2,3,4]])

# reshape
## a (2,3) matrix to a (6,1) array
np.array[([1,2,3],[2,3,4]]).reshape((6,1))
```

**Function that can do scalar and vector/matrix element-wise(on np array) operation**

```python
np.dot(x,y)
np.exp(x,y)
np.log(x,y)
# element-wise product
np.multiply(x,y)
# outer product
np.outer(x,y)
```


**Aggregation**

```python
# axis=0 means sum vertically (by column), axis=1 means sum by row
# keepdims make a column vector when axis=1
np.sum(x, axis=0, keepdims=True) 

# get norm 2 for each row
np.linalg.norm(x, axis=1, keepdims=True)

```

### Broadcast

+-*/ operation between two np.array will expand the second operand vector/scalar to the same dimension as the first operand and then do the element-wise operation.

```python

x = np.array[([1,2,3],[2,3,4]]) 
# x - 1  is the same as:
x - np.ones((2,3))

# x / np.array([2,3]) is the same as 
x / np.array[([2,2,2],[3,3,3]]) 
```


### A machine learning steps

```python
# preprocessing
## Reshape data

## Stardardize ()

# training
## initialize the parameters



```