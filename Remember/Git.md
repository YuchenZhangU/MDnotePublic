[toc]
# Git Questions and Cheatsheet
## Question

- How to use fork and pull request?
- If the local repo diverge with remote repo what to do?

## Cheatsheet

### Configurations

```bash
# editor
git config --global core.editor code

# autcrlf
## Windows: use carriage-return character and linefeed character for newlines
## Mac and Linux: use only linefeed charactere for newlines
## CRLF is escaped as \r\n
## form feed is escaped as \f - page break/indent 
git config --global core.autocrlf true # turn on auto convert lf to crlf, on Windows
git config --global core.autocrlf input # on Mac
git config --global core.autocrlf false # on Windows-only project

## Relove the problem that on window: "Filename too long"
git config core.longpaths true - for current folder
git config --system core.longpaths true - for all folder


```

### Basic Commands

git version 1.x:

![](https://i.stack.imgur.com/YfLUZ.jpg)

git version 2.x

![](https://i.stack.imgur.com/KwOLu.jpg)


```bash

#------ git status
git status ## check if there is any change working space vs the last commit

#------ git log
# show all branch graph with branch name highlighed
git log --all --graph --oneline --decorate

# check commits between two branch
git log master..origin/master 

# git add
git add . ## add all changed, new and deleted files
git add -u ## only update changed/deleted files, no new file will be added
git add --ignore-removal ## add all new and changed files

# git commit
git commit -m "a message"

# git diff
git diff ## compare work space with last commit
git diff --staged ## compare staged area with last commit
git diff commit1 commit2 ## compare two commit/branch
git diff commit1 commit2 path ## compare files in a specific path of commit


# git reset
git reset ## unstaged all files - last commit to overwirte staged area
## on commit - its a way to change commit history
## move the head to a commit
git reset HEAD~2 --soft ## last commit == the 3rd last commit, staged area and working space will not be changed. The last 2 commits will be deleted on next commit
git reset HEAD~2 --mixed ## staged area will be changed to match the 4rd last commit, but the working space will not be changed
git reset HEAD~2 --hard ## both staged area and working space will be changed

## on file
git reset HEAD~2 filepath ## unstaged a specific file - overwrite staging area with a commit's file

# git checkout
git checkout commit/branch ## overwrite work space and staging area with commit/branch
git checkout commit/branch path 

# git branch
git branch # show all local branch
git branch -av # show all local/remote branch and their latest commit info
```


### Connection

**remote**

```bash
# ---- git remote
## remote is way to tag the url of repos so we can easily access the repo with other command
git remote -v # verbose: list all remote repos' fetch/push url/ssh
git remote add <repoName> <url>
git remote rm <repoName>
git remote rename <oldName> <newName>

## change url
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git



# ------ http vs ssh connect
## better use ssh if you need read and write access

# clone with submodules
git --recursive -j8 _path 

# remeber username/password on windows
git config --global credential.helper wincred
```

**Delete/Track/Create Remote Branch**

[sync branch/tags](https://stackoverflow.com/questions/5480258/how-to-delete-a-git-remote-tag)

general syntax
`git push origin refs/heads/master:refs/heads/master`

```bash
# track an already created remote branch but not in local branch yet
## the following commmand will create a new branch called testBranch
git checkout --track origin/testBranch
## or
git checkout -b testBranch origin/testBranch
## or
git fetch origin/testBranch
git branch testBranch origin/testBranch
git checkout testBranch

# Deletes all stale remote-tracking branches under <origin>. These stale branches have already been removed from the remote repository referenced by <origin>
git remote prune origin

```

**Push Fetch Pull**

[git push diverged branch (merge vs rebase)](https://stackoverflow.com/questions/2452226/master-branch-and-origin-master-have-diverged-how-to-undiverge-branches)

```bash
# delete the latest remote commit (not suggest to use. using revert is safer)
git reset --hard HEAD~1
git push --force # git push origin +master 

# delete the remote branch
git push -d origin test-1 # delete the branch named 'test-1'


#-------- push ----------
git push test-1 # need to specify branch name explicitly when pushing the branch that does not er
git push <remote> --force # overwrite the remote branch even it diverge from the local branch

git push <remote> --all # push all branches to remote

git push <remote> --tags # push all tags to remote  

#-------- fetch --------
## When checkout a remote branch, you will be in a detached HEAD state
## You can think of them as read-only branches. 
git fetch <remote>
git fetch <remote> <branch>
git fetch --all --tags --prune # fetch all branch, tags. deleted stale branches
git branch -r # check remote branch that fetched

#-------- pull ----------
# git pull = git fetch && git merge
# pull from remote repos directly for all branch (fast forward pull)
git pull --all

# pull from remote repos directly for one branch (fast forward pull)
git pull

# = git fetch && git rebase
git pull --rebase


#---- git how to push diverged branch
# way 1 merge first, will result in non-linear history
git fetch
git merge origin/master # then resolve merge conflict and "add && commit"

# way 2 rebase, change history. Will keep linear history
# "git rebase <basebranch> <topicbranch>"
git rebase origin/master # then resolve conflict and "add"
git rebase --continue # diverged commits will rebased on origin/master

# More about git rebase
git pull --rebase # pull and rebase on the origin/master
git fetch && git rebase origin/master # the same as the last command
git config --global pull.rebase true # set rebase as default when pull
## for git < 1.7.9:
git config --global branch.autosetuprebase always


#----- git rebase
# interactive rebase
git rebase -i origin/master
```

### Advanced Git

#### Advanced Log

```bash
# show insert/delete lines count of each line
git log --stat 

# see who has done what commit
git shortlog

# graph of all branch with decorate of branch/tag/HEAD
git log  --all --decorate --oneline --graph

# a build-in graph interface 
gitk

# customize log format
# https://www.kernel.org/pub/software/scm/git/docs/git-config.html
git log --pretty=format:"%cn committed %h on %cd"
## John committed 400e4b7 on Fri Jun 24 12:30:04 2014 -0500
## John committed 89ab2cf on Thu Jun 23 17:09:42 2014 -0500
## Aside from letting you view only the information that you’re interested in, the --pretty=format:"<string>" option is particularly useful when you’re trying to pipe git log output into another command.

# Filter history
## By Amount
git log -3 # display most recent 3 commit
## By Date
git log --after="2014-7-1"
git log --before="yesterday"
git log --after="2014-7-1" --before="2014-7-4"
git log --since="2014-7-1" --until="2014-7-4" # the same as the last command

## By Author 
git log --author="John\|Mary" # commit by John or Mary. Accept a Regex
### git --committer work the similiar way

## By Message
git log --grep="JRA-224" # Accep a Regex
git log --gre="JRA-224" -i # Case insensitive

## By file
git log -- foo.py bar.py

## By content
git log -S"Hello, World!" # pass in string 
git log -G"Hello, World!" # pass in regex
###  This is a very powerful debugging tool, as it lets you locate all of the commits that affect a particular line of code. It can even show you when a line was copied or moved to another file.
## By Range
git log master..feature # show difference between 2 branches, show commits that is in feature but not in master
git log feature..master # show commit that is in master but no in feauture

## Merge Commit
git log --merges
git log --no-merges

```

#### Clean Workspace/Branch
[git prune/git remote prune](https://stackoverflow.com/questions/20106712/what-are-the-differences-between-git-remote-prune-git-prune-git-fetch-prune)

```bash
# removes objects that are no longer being referenced
git prune

# Deletes all stale remote-tracking branches under <origin>. These stale branches have already been removed from the remote repository referenced by <origin>
git remote prune origin

# delete a local branch
git branch -d branchName
# forcer detele a local branch
git branch -D branchName


# optimize .git size
git gc # Cleanup unnecessary files and optimize the local repository
```

#### Rebase vs Merge

```bash
# merge multipe commit into one
git merge <branchName> --squash 


#---- git rebase 
# use git rebase to squash multiple commits into one commit
## will edit a list of commit and use pick/squash/fixup/edit before each line to indicate what to do with each commit
## will squash up
git rebase -i HEAD~40 # interactive rebase on the last 42 commit
```

#### git stash

temporarily store the uncommited changes and apply the change anywhere later.

```bash
# save all uncommited changes (only include tracked files)
## you can see  `git log --all --graph --oneline`
git stash # or git stash save 

# list all statsh
git stash list
## stash@{0}: WIP on master: 049d078 added the index file
## stash@{1}: WIP on master: c264051 Revert "added file_size"
## stash@{2}: WIP on master: 21d80a5 added number to log

# apply the stash
git stash apply # apply the latest stash
git stash apply stash@{2} # apply a specific stash

# by default the file you staged before wasn't restage. To do that, you must run 
git stash apply --index

# drop a specific stash
git stash drop stash@{2}

# apply and drop
git stash pop

# do not save staged changes
git stash --keep-index

# include untracked file
git stash --include-untracked 
## or
git stash -u

# interactively select
git stash --patch

# apply stash and create a new branch
git stash branch <branch-name>


```


#### git tag

[what is tag](https://stackoverflow.com/questions/35979642/how-to-checkout-remote-git-tag)

**lightweight**

Just a pointer to a commit.
`git tag`

**annotated**

Annotated tags are stored as full objects in the Git database. They’re checksummed; contain the tagger name, email, and date; have a tagging message.
`git tag -a v1.4 -m "my version 1.4"`



```bash
# show tag info
git show v1.4

# tag a specific commit, given its checksum
git tag -a v1.2 9fceb02

# share tag(push tag to remote server)
git push origin v1.5 # v1.5 is the tag name

# push all tags to a remote
git push origin --tags

# general syntax for checkout a tag, and create a branch named version1.2
git checkout tags/v1.2 -b version1.2 

# if we checkout an branch, we will be in detached mode
git checkout v1.4 # will be in detached mode
## if you would like to continue work/commit based on current commit, create a new branch
git checkout -b newBranch

## or shorten the two commands into one:
git checkout -b newBranch v1.4

# delete local tag
git tag --delete v1.4 # git tag -d v1.4

# delete remote tag
git push -d origin v1.4

# pull all remote tag
git fetch --tags
``` 

#### Submodule

```bash
# add an submodule
git submodule add https://github.com/<user>/rock rock

# init the module
git submodule update --init --recursive

# clone the project first time, to download the submodule at the same time
git clone --recursive <project url>

```

Take an existing subfolder and turn it into an external dependency
[shrink the size of repo](https://stackoverflow.com/questions/5984428/how-to-delete-the-old-history-after-running-git-filter-branch)

[understawnd git filter branch]
https://manishearth.github.io/blog/2017/03/05/understanding-git-filter-branch/

```bash
# To rewrite the repository to look as if foodir/ had been its project root, and discard all other history
git filter-branch --subdirectory-filter foodir -- --all
##  Note the -- that separates filter-branch options from revision options, and the --all to rewrite all branches and tags.

## Or to filter a specific branch
git filter-branch --prune-empty --subdirectory-filter FOLDER-NAME  BRANCH-NAME 

## exclude the legacy history in .git/refs/original.
## way 1


## way2 

```

#### Advanced Log
```bash
# Find all action towards commit including commit, merge, checkout etc. Used to find lost commits
git reflog
```

### Git Workflow

**Centralized Workflow**
<small>Have a central repo every work local repos that sync with this central repo.</small>

```bash
# create central repo
ssh user@host git init --bare /path/to/repo.git

# every one copy this repo
git clone ssh://user@host/path/to/repo.git

# person one make several commits and push to the origin/master
git add . && git commit -m "first commit"
git push origin master

# person two make severl commits and push to the origin/master
# the push will fail because git person one has pushed new commits to origin/master
# master is now diverge from origin/master, cannot fast-forward merge origin/master into master need to merge these two first
git pull --rebase origin master
git add <some-file>
git rebase --continue

# once all conflicts are resolved, push to the remote
git push origin master
```