[toc]

**Series Outline**

- Neural Networks and Deep Learning
- Improve NN: Hyperparameter tuning, Regularization and Optimization
- Structuring your Machine Learning project
    train/dev/test
- Convolution Neural Networks
- NLP: Building sequence models
    + RNN

    + LSTM 

Notation

>
m - Number of training set

# Course One
![](./img/w1_CourseOutline.PNG)

## Week 1

### Introduction ot Deep Learning


![](./img/w1_ReLU.PNG)
**Relu** - common used
Rectified Linear Unit (most popular activation function right no)


**Supervised Learning Examples**

![](./img/w1_supervisedExamples.PNG)

![](./img/w1_CNNRNN.PNG)


#### **Why NN becomes powerful recently**

- Data
- Computation
- Algorithms


**Data**

![](./img/w1_scaling.PNG)

But for small training set, the performance of an algorithm is mosly depending the engineering on feature. The ordering of algorithns is unknown.

**Algorithms and Computation**

- Sigmoid -> ReLU: make gradient decent faster

![](./img/w1_Sigmoid_ReLU.PNG)

- Training NN is very iterative 




## Week 2 logistic regression (binary classification ) as neural network

Forward propagation
Backward propagation 


### Logistic regression

#### Image Data

3 matrces （RGB）
-> unroll a feature vector 

a 64 * 64 image will have nx = 64 * 64 * 3 features

![](./img/w2_XMatrix.png)

$X \in \mathbb{R}^{n_x * m}$

#### Hypothesis Function

Given X, want $\widehat{y} = P(y=1|x), 0 < y < 1$

$\widehat{y} = \sigma(\omega^Tx)$

$\sigma$ is sigmoid function
$\sigma(z) = \frac{1}{1 + e^{-x}}$

#### Cost Function

Given ${(x^{(0)},y^{(0)}),..., (x^{(m)},y^{(m)})}$, want $ \widehat{y}^{(i)} \approx y^{(i)}$.

- $y^{(i)}$ is the ground true label

Loss(error) function:
$L(\widehat{y},y) = 1/2 (\widehat{y}-y)^2$ 

Logistic regression **do not use this function** because the objective function for training (optimization) will becomes non-convex

Instead it uses 
$L(\widehat{y},y) = - (ylog\widehat{y} + (1-y)log(1-\widehat{y}))$
This function will give us a convex cost function.

**Loss function** is defined with regard to a single training example.
While **cost function** is with regard to whole training set.

$J(w,b) = \sum\limits_{i=1}^n L(\widehat{y}^{(i)},y^{(i)})$

#### Traning (Optimization - Gradient descend)

Find $w,b$ that minimize $J(w,b)$

> Since for logistic regression, the cost function is convex function, any intial point will work

$ \omega := \omega - \alpha \frac{\partial J}{\partial \omega}$
$ \omega := b - \alpha \frac{\partial J}{\partial b}$

> In code
$d\omega$ denotes $\frac{\partial J}{\partial \omega}$ 
$db$ denotes $\frac{\partial J}{\partial b}$


#### Derivative with computation graph

**Final output variable**

> In code, `dvar` denotes $\frac{\partial FinalOutputVariable}{\partial var} $ - the derivative of final output variable
dv denotes $\frac{\partial J}{\partial v}$

**Back Propagation**
**Chain Rule**
![](./img/w2_backprop.png)

#### Derivative of logistic regression

Review equations 

$z = \omega^Tx$
$\widehat{y} = a = sigma(z) = \frac{1}{1 - e^{-z}}$
$L(a,y) = - (yloga + (1-y)log(1-a))$
$J(w,b) = \frac{1}{m}\sum\limits_{i=1}^m L(\widehat{y}^{(i)},y^{(i)})$


![](./img/w2_log_derivatives.png)


$\frac{\partial}{\partial \omega_i}J(w,b) = \frac{1}{m}\sum\limits_{i=1}^m \frac{\partial}{\partial \omega_i} L(\widehat{y}^{(i)},y^{(i)})$

> When implementing deep learning algorithms for traning large data set, if use explicit for loop, you will find your code less efficient. Use technique called **vectorization** to get rid of the explicit for loops.


`i - idx of sample`
`j - idx of parameter`

**Equations**

$z^{(i)} = \omega^T x^{i}$
$a^{(i)} = \sigma(z^{(i)}) = \frac{1}{1 + e^{(-z^{(i)})}}$
$J =\sum -[y^{(i)}log(a^{(i)}) + (1-y^{(i)})log(1 - a^{(i)})]$

$\frac{\partial J}{\partial a}^{(i)} = -\frac{y^{(i)}}{a^{(i)}} + \frac{1-y^{(i)}}{1-a^{(i)}}$
$\frac{\partial a}{\partial z}^{(i)} = (1-a^{(i)})a^{(i)}$
**$\frac{\partial J}{\partial z}^{(i)} = \frac{\partial J}{\partial a}^{(i)} * \frac{\partial a}{\partial z}^{(i)} = a^{(i)}-y^{(i)}$**

$\frac{\partial z}{\partial w_j}^{(i)} = x_j^{(i)}$
$\frac{\partial z}{\partial b}^{(i)} = 1$
$\frac{\partial J}{\partial w_j}^{(i)} = \frac{\partial J}{\partial z}^{(i)} * \frac{\partial z}{\partial w_j}^{(i)} = (a^{(i)}-y^{(i)})x_j^{(i)}$
$\frac{\partial J}{\partial b}^{(i)} = \frac{\partial J}{\partial z}^{(i)} = (a^{(i)}-y^{(i)})$

#### Final Algorithm

$J=0; dw_1=0; dw_2=0; db=0;$
for i = 1 to m:
&emsp;$z^{(i)} = \omega^T x$
&emsp;$a^{(i)} = \sigma(z^{(i)}) = \frac{1}{1 + e^{(-z)}}$
&emsp;$J += -[y^{(i)}log(a^{(i)}) + (1-y^{(i)})log(1 - a^{(i)})]$
&emsp;$dz = a^{(i)} - y^{(i)}$
&emsp;$dw_1 += x_1^{(i)}dz^{(i)}$
&emsp;$dw_2 += x_2^{(i)}dz^{(i)}$
&emsp;$db += dz^{(i)}$

$J /= m$
$dw_1 /= m$
$dw_2 /= m$

> The implementation will use two loops. One loop through each training examples. Another loop through features.

### Python and Vectorization

#### Vectorization


```python
import numpy as np
np.dot(a,b)
```

> Whenever possible, avoid using explicit for-loops.
`numpy.dot` use Single Instruction Multiple Data(SIMD) to parallelize the computation. **Both CPU and GPU** can apply SIMD. Most modern CPU designs include SIMD instructions to improve the performance of multimedia use.


```python
# do exponential to each elements of a vector
import numpy as np
u = np.exp(v)
np.log(v)
np.maximum(v,0) # return a vec of size(v)
v**2
1/v

# Logistic Regression Algorithm Vectorized version
## Forard Propagation
X = [x_1, ... x_m]  # (nx, m)
y = [y_1,..., y_m]  # (1, m)
b   # scalar
Z = np.dot(w,X) + b   # (1, m). +b is called boardcasting in python
A = 1/(1 - np.exp(-z))  # (1,m)
J = -[np.dot(y, np.log(a)) + np.dot((1 - y), np.log(1-a))] # scalar

## Backpropagation
dZ = A - Y
dW = 1/m * np.dot(X, dZ)
db = 1/m * np.sum(dZ)

## Update
w = w - alpha * dW
b = b - alpha * dW
```

#### numpy Broadcasting
```python
a = [1,2,3,4]
a + 100 = a + [100, 100, 100, 100]

# For a (m,n) matrix, +-*/
## a (1,n) matrix. It will copy the (1,n) matrix m times into a (m,n) and then do element-wise operation.

## a (m,1) matrix. It will copy the (m,1) matrix n times into a (m,n) and then do element-wise operation.

cal = np.sum(axis=0) # sum matrix vertically
pct = 100*A/cal.reshape(1,4)
```
> reshape is very cheap to use (O(1)). Only use it make sure the matrix dimension is correct. 

#### Explanation of logistic regression cost function

$y \in {0,1}$ and $\widehat{y}$ is the probablity that $y=1$ we predict. Then,
for $y = 1$, $p(y|x) = \widehat{y}$
for $y = 0$, $p(y|x) = 1 - \widehat{y}$

Unify the equation:
$p(y|x) = \widehat{y}^y (1-\widehat{y})^{(1-y)}$
$log(p(y|x)) = ylog\widehat{y} + (1-y)log(1-\widehat{y})$

Would like to maximize $p(y|x)$ which the same as maximizing $log(p(y|x))$, thus we minimize:
$-[ylog\widehat{y} + (1-y)log(1-\widehat{y})]$

$p(y|X) = log \prod p(y|x) = \sum log(p(y|x))$

### Summary for Week 2

#### Concepts

>**softmax** - You can think of softmax as a normalizing function used when your algorithm needs to classify two or more classes.

**L1 loss**

$$L_1(\hat{y}, y) = \sum_{i=0}^m|y^{(i)} - \hat{y}^{(i)}| $$

**L2 loss**

#### Optimization

A lower cost doesn't mean a better model. You have to check if there is possibly overfitting. It happens when the training accuracy is a lot higher than the test accuracy.
In deep learning, we usually recommend that you:
Choose the learning rate that better minimizes the cost function.
If your model overfits, use other techniques to reduce overfitting. (We'll talk about this in later videos.)


>**Note**
Preprocessing the dataset is important.
You implemented each function separately: initialize(), propagate(), optimize(). Then you built a model().
Tuning the learning rate (which is an example of a "hyperparameter") can make a big difference to the algorithm. You will see more examples of this later in this course!

**Potential Options to improve**
- Play with the learning rate and the number of iterations
- Try different initialization methods and compare the results
- Test other preprocessings (center the data, or divide each row by its standard deviation)

## Week3 - Shallow Neural Network

![](./img/w3_NN.PNG)

>By convention, this is a two layer neural network

$x$ is a (3,1) vector
$W^{[1]}$ is a (3, 3) matrix
$a^{[1]}$ is a (3, 1) matrix
$W^{[2]}$ is a (1, 3) matrix

$W^{[i]}$ is a $(Na^{[i]}, Na^{[i-1]})$ matrix, where $a^{[0]}$ is x


### Concepts


Input Layer - $x = a^{[0]}$v
Hidden Layer - $a^{[i]}$
Output Layer - $y = a^{[n]}$

![](./img/w3_NN2.PNG)

$a^{[l]}_i$
$l$: layer number
$i$: nide in that layer

![](./img/w3_forward.PNG)

![](./img/w3_forward_vectorize.PNG)


### Activation Functions

**Sigmoid function**
$ 0 <= y <= 1 $

**tanh function** - always works better than sigmoid function
$ -1 <= y <= 1 $

![](./img/w3_activation.PNG)

> Almost never use $sigmoid$ function. Expect, if $y \in \{0,1\}$, the output layer will use sigmoid function and hidden layer will use $tanh$ function

>The tanh activation usually works better than sigmoid activation function for hidden units because the mean of its output is closer to zero, and so it centers the data better for the next layer

> One downside of Sigmoid/tanh function is that when Z is very large or small. the derivative becomes very small which will slow down the training of NN. 


**Rectified Linear Unit function**

> If you don't know what to use, just use ReLU function. But it's not gold rule. For specific project, you should try difference activation and see which works the best.

The derivative at 0 are unknow. But its very rarely to reach the exact 0. So make it either 0 or 1 would be fine.

**Leaky ReLU function**


![](./img/w3_activation2.PNG)

### Why Nonlinear Activation Functions

If we use linear activation the forward function is no different from a linear function.

> There is very rare that actvation function will be linear. For example the output layer's activation function can be linear if the output value is constraint to an specific interval.

### Derivative of activation function

**sigmoid**

$sig'(z) = a(1-a)$

**tanh**
$tanh'(z) = 1-a^2$


**ReLU**
$0, z < 0$
$1, z >= 0$

**Leaky ReLU**
$0.01, z < 0$
$1, z >= 0$



### Backpropagation

![](./img/w3_derivatives.PNG)



### Paramerter Initilization

If initialize all parameter to 0 will have all symetric breaking problem.

![](./img/w3_initialization.PNG)


**Results that initilize W with np.random.randn(a,b)**

```
Accuracy for 1 hidden units: 61.5 %
Accuracy for 2 hidden units: 70.5 %
Accuracy for 3 hidden units: 66.25 %
Accuracy for 4 hidden units: 90.75 %
Accuracy for 5 hidden units: 91.0 %
Accuracy for 20 hidden units: 91.5 %
Accuracy for 50 hidden units: 90.75 %
```

**Results that initilize W with `np.random.randn(a,b)*0.01`**

```
Accuracy for 1 hidden units: 67.5 %
Accuracy for 2 hidden units: 67.25 %
Accuracy for 3 hidden units: 90.75 %
Accuracy for 4 hidden units: 90.5 %
Accuracy for 5 hidden units: 91.25 %
Accuracy for 20 hidden units: 90.0 %
Accuracy for 50 hidden units: 90.25 %
```


## Week 4 - Deep Neural Network

### Debug - Dimension Check

$w^{[l]}: (n^{[l]}, n^{[l-1]})$

$b^{[l]}: (n^{[l]}, 1)$

$dw^{[l]}: (n^{[l]}, n^{[l-1]})$

$db^{[l]}: (n^{[l]}, 1)$

$z^{[l]}, a^{[l]}: (n^{[l]}, 1)$

$Z^{[l]}, A^{[l]}: (n^{[l]}, m)$

$dZ^{[l]}, dA^{[l]}: (n^{[l]}, m)$


### Why deep NN?

Can think of early layer of NN as detecting simply functions like edges.

![](./img/w4_imgReg.PNG)

Human neuron also works the similar way. It detect simple things like edges first and then combine them into more complex components.

From circuit theory

XOR ?
