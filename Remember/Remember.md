---
Type: summary
---

[toc]

## Programming Language

## Hello World Example
### java

```java
public class HelloWord {
    public static void main(String[] args) {
        system.out.printIn("Hello, World!");
    }
}
```

## basic
### python
```python
a_int = 2
a_str = "string"
a_dict = {'a': 1, 'b':2}
a_list = [1,2,3,4]
a_set = set(a_list)
b_set = {1,2,3,4}
a_tuple = (1,2,3)  #immutable, faster than list
```

### java

#### Complie and Run

```bash
# compile file
javac HelloWorld.java

#run binary file
java HelloWorld


javac-algs4 TestAlgs4.javas

java-algs4 TestAlgs4

java-algs4 edu.princeton.cs.algs4.StdDraw
java-algs4 edu.princeton.cs.algs4.StdAudio
```

```java
char a_char = 'G'
int[] a_array = {1,2,3,4};

```

#### Container

```java
// Array
int[] arr;
int[] arr = new int[10];
int[] arr = new int[]{1,2,3,4,5,6,7,8,9,10};

arr.length //length of arr

//ArrayList


```


### C++

```c++
// Array
int arr[5];
int arr[5] = {1,2,3,4,5};
int arr[] = {1,2,3,4,5};


```

## number

## string

## container
```java
int[] a_array = {1,2,3,4}
int array_len = a_array.length;
double[] b_array = new double[5];
/* By default array is asigned by reference*/
double[] c_array = b_array;
c_array = {1.0, 3.4} // now, b_array is {1.0, 3.4}
```
## function

### java
- Java function parameters are passed by value by default.
- method name can by overloaded
- A method have only one return value

```java
public static double sqrt(double c){

}

```

## library/module

### java
- standard system libraries (java.lang)
- imported system libraries (java.util.Arrays)


```java

```


## Programming Command


### Grunt
`npm install --save-dev grunt`
`npm install --save-dev grunt-sass`
`npm install --save-dev grunt-contrib-concat`
`npm install --save-dev load-grunt-tasks`
`npm install --save-dev grunt-contrib-jshint`
`npm install --save-dev grunt-contrib-watch`  - watch file for changes and when a change is detected to execute a specific series of tasks
`npm install --save-dev grunt-contrib-csslint`



`grunt`


```js

module.exports = function(grunt){
// load
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-concat');
// config
  grunt.initConfig({
    sass:{
      dist:{
        src: 'src/sass/style.scss',
        dest: 'dist/css/style.css'
      }
    },
    concat:{
      dist:{
        src: 'src/js/*.js',
        dest: 'dist/js/scripts.js'
      }
    }
  });

// register
  grunt.registerTask('default', [
    'sass',
    'concat'
  ]);
};
```

#### questions

- How require works?
- questions below grunt

- how the task runner can call the module? how grunt object works,(how the grunt object in the gruntfile.js works)
- sass, jshint, csslint, concat, watch - how they configed?
- what is 'yml' file? why yml?
- why "**/*.scss" ?

#### NPM

`module`
`require('module_name')`
`module.paths` - the folders in which sequence (current folder then parent folder) require search for "node_modules"
`require.resolve('module_name')` - don not execute file, return the full path for the module


### Express JS

```js


```

### React quick

```bash
npm install -g create-react-app
create-react-app mernCommentBox && cd mernCommentBox

```


### Heroku

```bash

# ------------- Create/Deploy ----------------
heroku login
heroku create # used under repository 
# a git remote (called heroku) is also created and associated with your local git repository.
git add .
git commit -m ""
git push heroku master
heroku open # open the deployed page
heroku open pagePath

heroku local


#------------- remote control (through dyno) -------
heroku run # test node environment
heroku run bash # test bash environment
heroku run node

# ----------- setting runtime ------------
.env # for external environment variable
# or use
heroku config:set TIMES=2
heroku config # check all Config Vars



#------------ Use Database -------------
heroku addons:create heroku-postgresql：hobby-dev
# now the connection str is in process.env.DATABASE_URL



# about domain name
https://devcenter.heroku.com/articles/custom-domains

```



#### Heroku - manage

```bash
heroku log --tail # check the latest log

heroku ps #  how many dynos are running using the ps command. Think of a dyno as a lightweight container that runs the command specified in the Procfile.
heroku ps:web=1 # Ensure that at least one instance of the app is running:

heroku ps:scale web=0 # close all dyno
heroku ps:scale web=1 # open one dyno
```


#### Heroku - provision

```bash
heroku addons:create papertrail
heroku addons # list all addons
heroku addons:open papertrail
```
### Tmux

https://danielmiessler.com/study/tmux/


```bash
brew install tmux

# session - window - panel
## session
tmux new -s session-name # create session
tmux a # attach to the first available session
tmux a -s session-name # attach to the sesion-name


tmux detach # detach a session (when in a session)
ctrl-b d

tmux ls # list all sessions 
tmux kill-session -t session-name
tmux kill-session -a # kill all session
ctrl-b $ # rename the current session

## window - when in a session
ctrl-b c # create a new window
ctrl-b , # rename the curretn window
ctrl-b n # go to next window
ctrl-b p # go to previour window 


## pane

ctrl-b %  vertical split
ctrl-b "  horizontal split
o  swap panes
q  show pane numbers
x  kill pane
+  break pane into window (e.g. to select text by mouse to copy)
-  restore pane from window
⍽  space - toggle between layouts

```


### Crypto

#### ETH


##### Basic
- Data Directory 
+ account
  * created by
   - new
   - key.prv
  * pass in password by
   - interactive console type in
   - pass a file with password on the first line and a single newline on the second line'''
     geth
```bash
brew tap ethereum/ethereum
brew install ethereum
```

Eth (cpp-ethereum)
```bash
brew update
brew upgrade
brew tap ethereum/ethereum
brew reinstall llvm

<At this point, close the terminal, and relaunch it.>

brew install leveldb libmicrohttpd cryptopp
brew install cpp-ethereum --devel --successful --verbose

brew linkapps cpp-ethereum

```

##### geth

```bash
# Create Account
geth account new
geth --password <passwordfile> account new # <passwordfile> - path to a file that have your password and a newline

# Fast download blockchain
## By default the blockchain and keystore will be at
## 	Mac: ~/Library/Ethereum
## 	Linux: ~/.ethereum
## 	Windows: %APPDATA%\Ethereum

geth --datadir <path> --rpc --fast --cache=1024 # <path> specify where to download the blockchain

# Manage Account
## The account index will order by the time created (lexicographic)
geth account list # account name in the form: <timeCreated>-<pukey>
geth account update <account> # change password, <account> can be index or public key hash

geth --unlock '0x407d73d8a49eeb85d32cf465507dd71d507100c1,0,5,e470b1a7d2c9c5c6f03bbaa8fa20db6d404a0c32' # unlock 4 accounts(hex, index, index ,hex)

# RPC
geth --rpc # default port: "http://localhost:8545"
geth --rpc --rpccorsdomain "http://localhost:3000" # add cross domain (if access from a browser)

# Mining
geth --mine --minerthreads=4 # geth cpu mining
geth --etherbase 1 --mine  2>> geth.log # 1 is index: second account by creation order OR
geth --etherbase '0xa4d8e9cae4d04b093aac82e6cd355b6b963fb7ff' --mine 2>> geth.log

## ethminer mining
ethminer --list-devices # list all available devices
ethminer # CPU mining, 
ethminer -G --opencl-device 1  # GPU mining using the second devices to mine
ethminer -M # CPU Benchmark min/mean/max: 0/0/0 H/s
ethminer -G -M --opencl-device 1 # Run GPU Benchmark

### optimize mining (for ATI GPU)
setx GPU_FORCE_64BIT_PTR 0
setx GPU_MAX_HEAP_SIZE 100
setx GPU_USE_SYNC_OBJECTS 1

setx GPU_MAX_ALLOC_PERCENT 100
setx GPU_SINGLE_ALLOC_PERCENT 100

ethminer -F http://asia1.nanopool.org:8888/hex/miner1 -G --opencl-platform 1

# Other 
geth --testnet --fast# local testnet
geth upgradedb
geth removedb
geth export <filename> # export the whole blockchain in binary format
geth import <filename> # import the whole blockchain in binary format
geth export <filename> 0,9999 # export the chain #0 to chain #9999, append the result to <filename>

```

##### Eth console (js)

```js

miner.start(8) // 8 is the number of threah in use
miner.stop()
miner.setEtherbase(eth.accounts[2])


miner.hashrate // checkcurrent hashrate
```


