
## Concepts

### Java bytecode vs MSIL

### JVM(java virtural machine) vs CLR (common language runtime)
they're both stack-based VM's


### what is machine  code?
The binary code that cpu can execute. 

>	Machine code, also called machine language, is a computer language that is directly understandable by a computer's CPU (central processing unit), and it is the language into which all programs must be converted before they can be run. Each CPU type has its own machine language, although they are basically fairly similar.

> After the source code for a program has been written by one or more humans in a programming language (e.g., C or C++), it is compiled (i.e., converted) into machine code by a specialized program called a compiler, or by an assembler in the case of assembly language. This machine code is then stored as an executable file (i.e., a ready-to-run program) and can be executed (i.e., run) by the operating system any time it is instructed to do so by another program or by a user.

> Machine code is extremely difficult for humans to read because it consists merely of patterns of bits (i.e., zeros and ones). Thus, programmers who want to work at the machine code level instead usually use assembly language, which is a human-readable notation for the machine language in which the instructions represented by patterns of zeros and ones are replaced with alphanumeric symbols (called mnemonics) in order to make it easier to remember and work with them (including reducing the chances of making errors). In contrast to high-level languages (e.g., C, C++, Java, Perl and Python), there is a nearly one to one correspondence between a simple assembly language and its corresponding machine language.

> Programs for the first electronic computers were written directly in machine code. However, the development of assembly language from the 1950s led to a large increase in programmer productivity. Initially, programs written in assembly language programs were hand-translated into machine code, but this tedious task was later eliminated by the development of assemblers to automate the translations.

For Assembly program: 
assembly code -> machine code (using assembler)

For C/C++
c/c++ code -> machine code (using compiler) -> executable file (using linker to link different object code(pieces of machine code))

For Java
Java code -> Java bytecode (using java compiler) -> machine code (using JIT compiler, JVM)
This way, Java bytecode is architecture independent, they can run on ARM/Intel/MIPS

### Machine code vs Assembly code vs object code 
8B 5D 32 is machine code

mov ebx, [ebp+32h] is assembly

lmylib.so containing 8B 5D 32 is object code


### What is linking

Linking refers to the creation of a single executable file from multiple object files. In this step, it is common that the linker will complain about undefined functions (commonly, main itself). During compilation, if the compiler could not find the definition for a particular function, it would just assume that the function was defined in another file. If this isn't the case, there's no way the compiler would know -- it doesn't look at the contents of more than one file at a time. The linker, on the other hand, may look at multiple files and try to find references for the functions that weren't mentioned. 

You might ask why there are separate compilation and linking steps. **First**, it's probably easier to implement things that way. The compiler does its thing, and the linker does its thing -- by keeping the functions separate, the complexity of the program is reduced. **Another (more obvious) advantage** is that this allows the creation of large programs without having to redo the compilation step every time a file is changed. Instead, using so called "conditional compilation", it is necessary to compile only those source files that have changed; for the rest, the object files are sufficient input for the linker. **Finally**, this makes it simple to implement libraries of pre-compiled code: just create object files and link them just like any other object file. (The fact that each file is compiled separately from information contained in other files, incidentally, is called the "separate compilation model".) 

To get the full benefits of condition compilation, it's probably easier to get a program to help you than to try and remember which files you've changed since you last compiled. (You could, of course, just recompile every file that has a timestamp greater than the timestamp of the corresponding object file.) If you're working with an integrated development environment (IDE) it may already take care of this for you. If you're using command line tools, there's a nifty utility called make that comes with most *nix distributions. Along with conditional compilation, it has several other nice features for programming, such as allowing different compilations of your program -- for instance, if you have a version producing verbose output for debugging. 

Knowing the difference between the compilation phase and the link phase can make it easier to hunt for bugs. Compiler errors are usually syntactic in nature -- a missing semicolon, an extra parenthesis. Linking errors usually have to do with missing or multiple definitions. If you get an error that a function or variable is defined multiple times from the linker, that's a good indication that the error is that two of your source code files have the same function or variable. 

### what is make file


## Java Compiler

 Java code need to be compile twice.
 - Java programs need to be compiled to bytecode. (Using javac, HelloWorld.java -> HelloWorld.class)
- When the bytecode is run, it needs to be converted to machine code. (Using JIT(just-in-time) compiler)

>The Java classes/bytecode are compiled to machine code and loaded into memory by the JVM when needed the first time. This is different from other languages like C/C++ where programs are to be compiled to machine code and linked to create an executable file before it can be executed.



## Java vs C++ vs C#

java:
java -> java bytecode -> machine code
c# -> common intermediate language -> machine code
c++ -> c++ -> machine code (link with executable)

Java Compiler: It compiles JAVA code into an intermediate form called bytecode (Java bytecode). When you run compiled Java binary, it is compiled again to native machine codes using another compiler called Just In Time Compiler (Just-in-time compilation).

C Compiler: It compiles C code to native machine code. There is no just in time compilation involved.

C# Compiler: It compiles C# code to an intermedite form called MSIL, which was later renamed as Common Intermediate Language (Common Intermediate Language). Similar to Java, CIL code is compiled to native machine code upon execution.