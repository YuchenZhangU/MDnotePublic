[toc]



## C
### Basic typing

```c
float x = 0 has an implicit typecast from int to float.
float x = 0.0f does not have such a typecast.
float x = 0.0 has an implicit typecast from double to float.

```

### Dynamic memory allocator
void *malloc(size_t size)

size − This is the size of the memory block, in bytes.

**Return value**
On success, returns the pointer to the beginning of newly allocated memory. To avoid a memory leak, the returned pointer must be deallocated with `free()` or `realloc()`.

On failure, returns a null pointer.

```c
 int *p1 = malloc(4*sizeof(int));
 if(p1) {
    for(int n=0; n<4; ++n) // populate the array
        p1[n] = n*n;
    for(int n=0; n<4; ++n) // print it back out
        printf("p1[%d] == %d\n", n, p1[n]);
}
free(p1);
```

### Generate Random Number



```c

//Use C program to generate random numbers
#include <stdio.h>
#include <stdlib.h>
#include<time.h>

int main(void)
{
    // This program will create different sequence of 
    // random numbers on every program run 
 
    // Use current time as seed for random generator
    srand(time(0));
 
    for(int i = 0; i<5; i++)
        printf(" %d ", rand());

    // Generate random  number between [0,1]
    for(int i = 0; i<5; i++)
        printf(" %d ", rand()/(float)RAND_MAX);
 
    return 0;
}

```

## CPP

### scope operator ::

- Append after class name to access the class'
    + static member
    + function definition
    + type define in this class scope `typedef`
    + enum type define in this class `enum color{blue, red}`
- Different from **dot operator** in that dot operator is used to access member of an object (an instance of class not class itself).

### Static

#### Static Member

- Ao matter how many objects of the class are created, there is only one copy of the static member. (Share through the instance of a class)
- Initialized to zero when the first object is created, if no other initilization is present.
- Initialized outside the class.

```c++
#include <iostream>
 
using namespace std;

class Box {
   public:
      static int objectCount;
      
      // Constructor definition
      Box(double l = 2.0, double b = 2.0, double h = 2.0) {
         cout <<"Constructor called." << endl;
         length = l;
         breadth = b;
         height = h;
         
         // Increase every time object is created
         objectCount++;
      }
      double Volume() {
         return length * breadth * height;
      }
      
   private:
      double length;     // Length of a box
      double breadth;    // Breadth of a box
      double height;     // Height of a box
};

// Initialize static member of class Box
int Box::objectCount = 0;

int main(void) {
   Box Box1(3.3, 1.2, 1.5);    // Declare box1
   Box Box2(8.5, 6.0, 2.0);    // Declare box2

   // Print total number of objects.
   cout << "Total objects: " << Box::objectCount << endl;

   return 0;
}
```

#### Static Function

- Independent of any particular object of the class. Can be called even if no objects of the class exist and the static functions are accessed using only the class name and the scope resolution operator ::.
- A static member function can only access static data member, other static member functions and any other functions from outside the class.
- Static member functions have a class scope and they do not have access to the this pointer of the class?

### Declaration

```c++
struct C {
    int member; // "int" is the type specifier 
                // "member" is the declarator
} obj, *pObj = &obj;
// "struct C { int member; }" is the type specifier
// declarator "obj" defines an object of type struct C
// declarator "*pObj" declares a pointer to C,
// initializer "= &obj" provides the initial value for that pointer

int a = 1, *p = NULL, f(void), (*pf)(double);
// the type specifier is "int"
// declarator "a" defines an object of type int
//   initializer "=1" provides its initial value
// declarator "*p" defines an object of type pointer to int
//   initializer "=NULL" provides its initial value
// declarator "f(void)" declares a function taking void and returning int
// declarator "(*pf)(double)" defines an object of type pointer
//   to function taking double and returning int
 
int (*(*foo)(double))[3] = NULL;
// the type specifier is int
// 1. declarator "(*(*foo)(double))[3]" is an array declarator:
//    the type declared is "/nested declarator/ array of 3 int"
// 2. the nested declarator is "*(*foo)(double))", which is a pointer declarator
//    the type declared is "/nested declarator/ pointer to array of 3 int"
// 3. the nested declarator is "(*foo)(double)", which is a function declarator
//    the type declared is "/nested declarator/ function taking double and returning
//        pointer to array of 3 int"
// 4. the nested declarator is "(*foo)" which is a (parenthesized, as required by
//        function declarator syntax) pointer declarator.
//    the type declared is "/nested declarator/ pointer to function taking double
//        and returning pointer to array of 3 int"
// 5. the nested declarator is "foo", which is an identifier.
// The declaration introduces the identifier "foo" to refer to an object of type
// "pointer to function taking double and returning pointer to array of 3 int"
// The initializer "= NULL" provides the initial value of this pointer.
 
// If "foo" is used in an expression of the form of the declarator, its type would be
// int.
int x = (*(*foo)(1.2))[0];

```

### Pointer and Reference

**Difference**

> **Pointers**: A pointer is a variable that holds memory address of another variable. A pointer needs to be dereferenced with * operator to access the memory location it points to.

> **References**: A reference variable is an alias, that is, another name for an already existing variable. A reference, like a pointer is also implemented by storing the address of an object.

```c++
int i = 3; 

// A pointer to variable i (or stores
// address of i)
int* ptr = &i; 

// A reference (or alias) for i.
int& ref = i; 
```

**Difference**
- Pointer can be **reassigned**, reference cannot be re-assigned, and must be assigned at initilization
- **Memory Address**: A pointer has its own memory address and size on the stack whereas a reference shares the same memory address (with the original variable) but also takes up some space on the stack.
- Pointer can be assigned **NULL** directly, whereas reference cannot.
- **Indirection**: You can have pointers to pointers to pointers offering extra levels of indirection. Whereas references only offer one level of indirection.
- **Arithmetic operations**: Various arithmetic operations can be performed on pointers whereas there is no such thing called Reference Arithmetic.(but you can take the address of an object pointed by a reference and do pointer arithmetics on it as in &obj + 5).)


**Use references**
- In function parameters and return types.
**Use pointers:**
- To implement data structures like linked list, tree, etc and their algorithms.
- Use pointers if  pointer arithmetic or passing NULL-pointer is needed. For example for arrays (Note that array access is implemented using pointer arithmetic).


**Used as parameter**

> Use pointers if you want to do pointer arithmetic with them (e.g. incrementing the pointer address to step through an array) or if you ever have to pass a NULL-pointer.
> Use references otherwise.

```c++
class A{
    int add(int x, int y){
        return x+y;
    }
}

void test(A& func){
    std::cout << func.add(10,12);
}

void test2(A* func){
    std::cout << func->add(10,12);
}

int main(){
    A obj;
    test(obj);
    test2(&obj);
}

```
### Vector


**vector::data()**

```c++
 //Returns a direct pointer to the memory array
std::vector<int> ivec(5);
int* p = ivec.data();
*p = 10;
p[1] = 100; 
//now ivec[0] equal 10, ivec[1] equal 100

```


### typedef

Typedef declaration does not introduce a distinct type, it only establishes a synonym for an existing type, thus typedef names are compatible with the types they alias. 
```c++
//A typedef for a VLA can only appear at block scope. The length of the array is evaluated each time the flow of control passes over the typedef declaration, as opposed to the declaration of the array itself:
void copyt(int n)
{
    typedef int B[n]; // B is a VLA, its size is n, evaluated now
    n += 1;
    B a; // size of a is n from before +=1
    int b[n]; // a and b are different sizes
    for (int i = 1; i < n; i++)
        a[i-1] = b[i];
}


//typedef name may be an incomplete type, which may be completed as usual:
typedef int A[]; // A is int[]
A a = {1, 2}, b = {3,4,5}; // type of a is int[2], type of b is int[3]
```


### Inline Function

Pros :- 
1.	It speeds up your program by avoiding function calling overhead.
2.	It save overhead of variables push/pop on the stack, when function calling happens.
3.	It save overhead of return call from a function.
4.	It increases locality of reference by utilizing instruction cache.
5.	By marking it as inline, you can put a function definition in a header file (i.e. it can be included in multiple compilation unit, without the linker complaining)

Cons :-
1.	It increases the executable size due to code expansion. 
2.	C++ inlining is resolved at compile time. Which means if you change the code of the inlined function, you would need to recompile all the code using it to make sure it will be updated
3.	When used in a header, it makes your header file larger with information which users don’t care.
4.	As mentioned above it increases the executable size, which may cause thrashing in memory. More number of page fault bringing down your program performance.
5.	Sometimes not useful for example in embedded system where large executable size is not preferred at all due to memory constraints.

When to use - 
Function can be made as inline as per programmer need. Some useful recommendation are mentioned below-
1. Use inline function when performance is needed.
2. Use inline function over macros.
3. Prefer to use inline keyword outside the class with the function definition to hide implementation details.


Key Points - 
1.	It’s just a suggestion not compulsion. Compiler may or may not inline the functions you marked as inline. It may also decide to inline functions not marked as inline at compilation or linking time.

### Const Member Function

Not allow to modify the object on which they are called.


```c++

#include<iostream>
using namespace std;

class Test {
    int value;
public:
    Test(int v = 0) {value = v;}
     
    // We get compiler error if we add a line like "value = 100;"
    // in this function.
    int getValue() const {return value;}  
};
 
int main() {
    Test t(20);
    cout<<t.getValue();
    return 0;
}
```

### function pointer

```c++
void foo(){
    std::cout << "Hello" << std::endl;
}

void (*funcPtr)() = foo;
funcPtr(); //the same as calling foo();
```


## Questions 

### C++, What does the colon after a constructor mean? **initilialization list**

1. Calling base class constructors
2. Initialising member variables before the body of the constructor executes. We cannot change the value of a const variable in the constructor, because it is marked as const. So you can use the initialization list.

### void pointer in C

A void pointer is a pointer that has no associated data type with it. A void pointer can hold address of any type and can be typcasted to any type.

```c++
int a = 10;
char b = 'x';
 
void *p = &a;  // void pointer holds address of int 'a'
p = &b; // void pointer holds address of char 'b'


int main()
{
    int a[2] = {1, 2};
    void *ptr = &a;
    ptr = ptr + sizeof(int);
    printf("%d", *(int *)ptr);
    return 0;
}
//output 2
```


### What is the difference between int* p and int *p declaration?
There is no difference.

It's a matter of notation, not semantics. The second is less misleading, because

`int *a, b;`
is clearly declaring an int* and an int, whereas

`int* a, b;`
looks as if it's declaring two pointers, when it's really doing the same thing as above.


### What is the difference between `stuct Foo{};` and `typedef struct {} Foo;`
In C++, there is only a subtle difference. It's a holdover from C, in which it makes a difference.

The C language standard (C89 §3.1.2.3, C99 §6.2.3, and C11 §6.2.3) mandates separate namespaces for different categories of identifiers, including tag identifiers (for struct/union/enum) and ordinary identifiers (for typedef and other identifiers).

If you just said:

```c++
struct Foo { ... };
Foo x;
```
you would get a compiler error, because Foo is only defined in the tag namespace.

You'd have to declare it as:

`struct Foo x;`
Any time you want to refer to a Foo, you'd always have to call it a struct Foo. This gets annoying fast, so you can add a typedef:

```c++
struct Foo { ... };
typedef struct Foo Foo;
```
Now both struct Foo (in the tag namespace) and just plain Foo (in the ordinary identifier namespace) both refer to the same thing, and you can freely declare objects of type Foo without the struct keyword.

The construct:

`typedef struct Foo { ... } Foo;`
is just an abbreviation for the declaration and typedef.

Finally,

`typedef struct { ... } Foo;`
declares an anonymous structure and creates a typedef for it. Thus, with this construct, it doesn't have a name in the tag namespace, only a name in the typedef namespace. This means it also cannot be forward-declared. If you want to make a forward declaration, you have to give it a name in the tag namespace.

In C++, all struct/union/enum/class declarations act like they are implicitly typedef'ed, as long as the name is not hidden by another declaration with the same name.

> Bottomline: Only have difference in C, because in C struct is only defined in the tag namespace.