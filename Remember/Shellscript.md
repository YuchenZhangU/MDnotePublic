[toc]

# Shell Script

## Bash / Linux Command

### Basic
```bash

# Basic commands
echo $0 # check what shell you are using
cd ~ # go to root directory
cd # go to root folder
cd - # go back to previous folder
ls
ls -l
rm
rm -r
rm -rf
mv
pwd
cp
cat <path> # output file of given <path> contain on shell
touch <path> # create file of give <path>
tail -n <path> # output only the last n rows of file 
head -n <path> # output only the top n rows of file
pushd <path> # push the <path> into dirs list 
pushd +n # make the nth (zero-based)
popd # delete the top element of dirs list
popd +n # delete the nth element of dirs list
dirs # show current dirs list

# search & filter
find ./Dropbox/ -name "*.json" # find all json file in Dropbox folder
grep "/[0-9]+/g" test.json # use regular expression to find all lines that contains number in test.json file
sed s/;/:/g test.json # replace all ; with : in test.json file



# set environment variable
## set single variable
echo "export NAME='CharZ'" >> .bash_profile
source .bash_profile # execute .bash_profile
echo $NAME  # NAME is now a environment variable, $ before NAME let system to know its a variable
## set PATH
echo "export PATH=$PATH:/path/to/your/file" >> .bash_profile

```

### System 

```bash
du -sch * # list all file/folder size in human readable format
```

### grep - regular expression print

```bash
grep '^test' test.txt # find line start with test
grep --color=auto 'test' test.txt # add color to matched text 
grep -C 1 'test' test.txt # show 1 line before and after the match
grep -B 1 'test' text.txt # show 1 line before the match
grep -A 1 'test' text.txt # show 1 line after the match
grep -v 'test' test.txt # inverse match
grep -n 'test' test.txt # show line number
grep -b 'test' test.txt # show bit offset of the found match
grep -e test1 -e test2 test.txt # find line with test1 or test2
grep -v -e test1 -e test2 test.txt # find line without test and without test2
grep -r test * # recursive match all file in folders
```

### sed

### awk

## Shell Programming
