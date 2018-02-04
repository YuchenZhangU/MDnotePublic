[toc]

## questions?

- LD_LIBRARY_PATH
- LIBRARY_PATH
- test exe can run on window?
- how to link static library?

## C++ compliation

- preprocessing
- compilation
- assemble
- linking

```bash
gcc -o hello.exe hello.c

# four steps
# 1 preprocessing. #include #define will be processed, convert to expanded source code *.i
cpp hello.c >  hello.i

# 2 compliation. pre-processed code -> assembly code for a specific cpu
gcc -S hello.i

# 3 assemble. assembly code -> machine code
as -o hello.o hello.s

# 4 linking. link object code with the library code production executable file (.exe)
ld -o hello.exe hello.o ...libraries...


# verbose mode
gcc -v -o hello.exe hello.c

# list the contents of a library via "nm filename".
nm main.exe

```

## Headers (.h), Static Libraries (.lib, .a) and Shared Library (.dll, .so)

**Static Library**
> When your program is linked against a static library, the machine code of external functions used in your program is copied into the executable. A static library can be created via the archive program "ar.exe".

**Shared Library**
> When your program is linked against a shared library, only a small table is created in the executable. Before the executable starts running, the operating system loads the machine code needed for the external functions - a process known as dynamic linking.

### include-paths, library-paths

[make static and dynamic libs](http://www.adp-gmbh.ch/cpp/gcc/create_lib.html)

When compiling the program, the compiler needs the header files to compile the source codes; the linker needs the libraries to resolve external references from other object files or libraries.

- PATH: For searching the executables and run-time shared libraries (.dll, .so).

**Header Files**

`-I<dir>` to include path for header files.

Or Use environment variable: 

`CPATH`: For searching the include-paths for headers. It is searched after paths specified in `-I<dir>` options. `C_INCLUDE_PATH` and `CPLUS_INCLUDE_PATH` can be used to specify C and C++ headers if the particular language was indicated in pre-processing.

**Library**

`-L<dir>` to provide library directory.

On Unix, `-lxxx` to provide specific file in the directory for `libxxx.a`

On Windows, `-lxxx.lib` to provide specific file in the directory for `libxxx.lib`

`LIBRARY_PATH`: For searching library-paths for link libraries. It is searched after paths specified in `-L<dir>` options.
- framework path ?

```bash
# check include path
cpp -v

# check library path

```
**Intel Compiler**

- LD_LIBRARY_PATH specifies the location for shared objects.
- PATH specifies the directories the system searches for binary executable files.
- ICCCFG specifies the configuration file for customizing compilations when invoking the compiler using icc.
- ICPCCFG specifies the configuration file for customizing compilations when invoking the compiler using icpc.
- Several environment variables are supported to specify the location for temporary files. The compiler searches for the following variables in the order specified: TMP, TMPDIR, and TEMP. If none of these variables are found, temporary files are stored in /tmp.
- IA32ROOT (IA32-based systems) points to the directory containing the bin, lib, include and substitute header directories.
- IA64ROOT (Itanium®-based systems) points to the directory containing the bin, lib, include and substitute header directories.

### nm,  file 
```bash
# find the type of the file
file hello.o
file hello.exe

# find the library included in the executable file
nm hello.o
nm hello.exe
## second column meaning
## 'T' indicates a function that is defined
## 'U' means a function is undefined and need to resolved by the linker


# list link library
## on windows
ldd hello.exe

## on macl
otool -L hello.exe
```

## Create static and shared library



## Cmake

### Basic Example
[CMake](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html)

>target: pre-req-1 pre-req-2 ...
	command

**Example**

```makefile
all: hello.exe # phony target, always run

hello.exe: hello.o # file target, checked against its pre-requisite for out-of-date-ness
	 gcc -o hello.exe hello.o

hello.o: hello.c # file target, checked against its pre-requisite for out-of-date-ness
	 gcc -c hello.c
     
clean: # no pre-requisites, phony target, always run
	 rm hello.o hello.exe

```

The target and pre-requisites are separated by a colon (:). The command must be preceded by a tab (NOT spaces).

When make is asked to evaluate a rule, it begins by finding the files in the prerequisites. If any of the prerequisites has an associated rule, make attempts to update those first.

If the pre-requisite is not newer than than target, the command will not be run. In other words, the command will be run only if the target is out-dated compared with its pre-requisite. For example, if we re-run the make command:

**Example on using the make file**
```bash
# by default, the rule(target) "all" will be envoked
make

# call other rul(target)
make clean
```

### Phony Targets (or Artificial Targets)

A target that does not represent a file is called a phony target. For example, the "clean" in the above example, which is just a label for a command. If the target is a file, it will be checked against its pre-requisite for out-of-date-ness. Phony target is always out-of-date and its command will be run. The standard phony targets are: all, clean, install.


### Variables

A variable begins with a $ and is enclosed within parentheses (...) or braces {...}. Single character variables do not need the parentheses. For example, $(CC), $(CC_FLAGS), $@, $^.

### Automatic variables are set by make after a rule is matched. There include:

`$@`: the target filename.
`$*`: the target filename without the file extension.
`$<`: the first prerequisite filename.
`$^`: the filenames of all the prerequisites, separated by spaces, discard duplicates.
`$+`: similar to `$^`, but includes duplicates.
`$?`: the names of all prerequisites that are newer than the target, separated by spaces.


### Virtual Path - VPATH & vpath
You can use VPATH (uppercase) to specify the directory to search for dependencies and target files. For example,

```bash
# Search for dependencies and targets from "src" and "include" directories
# The directories are separated by space
VPATH = src include
```

You can also use vpath (lowercase) to be more precise about the file type and its search directory. For example,
```bash
# Search for .c files in "src" directory; .h files in "include" directory
# The pattern matching character '%' matches filename without the extension
vpath %.c src
vpath %.h include

```

### Makefile
[A short tutorial](https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html)

**Syntax of Rules**
A general syntax for the rules is:
target1 [target2 ...]: [pre-req-1 pre-req-2 ...]
	[command1
	 command2
	 ......]

Automatic Variables
Automatic variables are set by make after a rule is matched. There include:
`$@`: the target filename.
`$*`: the target filename without the file extension.
`$<`: the first prerequisite filename.
`$^`: the filenames of all the prerequisites, separated by spaces, discard duplicates.
`$+`: similar to $^, but includes duplicates.
`$?`: the names of all prerequisites that are newer than the target, separated by spaces.

## GDB prompt commands

https://ccrma.stanford.edu/~jos/stkintro/Useful_commands_gdb.html

You don't need to know the command if you use vscode. Go to [cheatsheet](http://darkdust.net/files/GDB%20Cheat%20Sheet.pdf) for more commands

```bash
# when compile executable file, you have to add -g to generate gdb Debugging Symbol (.dSYM folder)
g++ -g -o main.exe main.cpp

# start debug main.exe
gdb main.exe

# commands
q # **quit** the program
r # **run** the program
k # **kill** the runing program
b main # **break** at function main
n # go to **next** line
l # **list** the code
info local # print all local variables
```