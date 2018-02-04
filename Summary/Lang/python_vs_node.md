## Ultility

```python
type(1)  #
```

```js
typeof({}) // object
```

## Date Type

### **python**
```python
True
False
```

### **javascript**
```js
true
false
```

## Container

**python**
```python
# judge if is in the dic or list
if x in dic:
    print 'yes, x is in dic'

# set
## initilize
set_a = set([1,2,3])
set_b = {1,2,3}

## methods
## -- add
set_a.add(4) # set([1,2,3,4])

## -- remove
set_b.remove(1)

## subset/superset
set_b.issubset(set_a) # True
set_a.issuperset(set_b) # True
set_a.intersection(set_b) # set([2,3])

## -- difference
x = set(["Postcard", "Radio", "Telegram"])
y = set(["Radio","Television"])
print( x.difference(y) ) # set(['Postcard', 'Telegram']) in x but not in y
print( y.difference(x) ) # in y but not in x


```



## Basic computation

### **python**

<table border="1">
	<caption>Arithmetic operators in Python</caption>
	<tbody>
		<tr>
			<th>Operator</th>
			<th>Meaning</th>
			<th>Example</th>
		</tr>
		<tr>
			<td>+</td>
			<td>Add two operands or unary plus</td>
			<td>x + y<br>
				+2</td>
		</tr>
		<tr>
			<td>-</td>
			<td>Subtract right operand from the left or unary minus</td>
			<td>x - y<br>
				-2</td>
		</tr>
		<tr>
			<td>*</td>
			<td>Multiply two operands</td>
			<td>x * y</td>
		</tr>
		<tr>
			<td>/</td>
			<td>Divide left operand by the right one (always results into float)</td>
			<td>x / y</td>
		</tr>
		<tr>
			<td>%</td>
			<td>Modulus - remainder of the division of left operand by the right</td>
			<td>x % y (remainder of x/y)</td>
		</tr>
		<tr>
			<td>//</td>
			<td>Floor division - division that results into whole number adjusted to the left in the number line</td>
			<td>x // y</td>
		</tr>
		<tr>
			<td>**</td>
			<td>Exponent - left operand raised to the power of right</td>
			<td>x**y (x to the power y)</td>
		</tr>
	</tbody>
</table>

---
<table border="1">
	<caption>Bitwise operators in Python</caption>
	<tbody>
		<tr>
			<th>Operator</th>
			<th>Meaning</th>
			<th>Example</th>
		</tr>
		<tr>
			<td>&amp;</td>
			<td>Bitwise AND</td>
			<td>x&amp; y = 0 (<code>0000 0000</code>)</td>
		</tr>
		<tr>
			<td>|</td>
			<td>Bitwise OR</td>
			<td>x | y = 14 (<code>0000 1110</code>)</td>
		</tr>
		<tr>
			<td>~</td>
			<td>Bitwise NOT</td>
			<td>~x = -11 (<code>1111 0101</code>)</td>
		</tr>
		<tr>
			<td>^</td>
			<td>Bitwise XOR</td>
			<td>x ^ y = 14 (<code>0000 1110</code>)</td>
		</tr>
		<tr>
			<td>&gt;&gt;</td>
			<td>Bitwise right shift</td>
			<td>x&gt;&gt; 2 = 2 (<code>0000 0010</code>)</td>
		</tr>
		<tr>
			<td>&lt;&lt;</td>
			<td>Bitwise left shift</td>
			<td>x&lt;&lt; 2 = 40 (<code>0010 1000</code>)</td>
		</tr>
	</tbody>
</table>

```python
5/3 = 1
5%3 = 2


# logic operation
## XOR, exclusive or, bitwise operator, return 1 only if two number different, one 0 and one 1
## commutative, associative and self-inverse.
## a^b=b^a, (a^b)^c=a^(b^c), a^a=0, a^0 =a
## application: [a,b,c,a,b] => r=0 for i in list: r = r^i => r = c
2^3 # 10 XOR 11 = 01  


## Binary
bin(9) #'0b1001' convert to string
bin(0).count('1') # count how many 1 in the string

```

```js
5/3=1.66667
5%3=1
```


## Pythin Niche

```python
# every other elements of list or str
str = 'you are good'
str[::2] # equal to str[0::2] = 'yuaego'
str[1::2] 

# reverse list
str[::-1] # str[100] will get IndexError, but str[100::-1] will not


```