[toc]

## Remote Editing Throught SSH

### Basic SSH
http://www.rebol.com/docs/ssh-auto-login.html

```bash
ssh guotong@r129.244.56.164
```

**create ssh key pair to auto login withou password**

```bash
# auto login in remote server without password
## At you machine, generate ssh key pair
ssh-keygen -C "yuchen-zhang@utulsa"
## hit enter
## hit enter agian, don't need to set passphrase
## get two file id_rsa id_rsa.pub

## change access right
chmod 600 id_rsa

## push public key to remote
rsync -av ./id_rsa.pub guotongren@remote_IP:~/.ssh

## login to the server and put public key into ~/.ssh/authorized_keys
ssh guotongren@remote_IP
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
rm ~/.ssh/id_rsa.pub

```

**Put the following file in the ~/.ssh/config** (to create an ssh tunnel between local and remote with short cut `ssh -v Rami`)

```config
Host Rami
    HostName 129.244.56.164
    User guotongren
    ForwardAgent yes
    RemoteForward 52698 127.0.0.1:52698
```

### Sync files

**rsync**

```bash
# use rsync to push file into remote machine
rsync -av . guotongren@129.244.56.164
```

**scp**

```bash
scp ./main.exe guotongren@129.244.56.164:~/test/

scp -r ./test guotongren@129.244.56.164:~/test/
```

### Open File on Remote with Vscode 

#### Set up at local machine
- intall vscode plugin "remote-vscode"
`ext intall remote-vscode`

- add setting to vscode
```json
//-------- Remote VSCode configuration --------

// Port number to use for connection.
"remote.port": 52698,

// Launch the server on start up.
"remote.onstartup": true

// Address to listen on.
"remote.host": "127.0.0.1"

// If set to true, error for remote.port already in use won't be shown anymore.
"remote.dontShowPortAlreadyInUseError": false
```

- start a server on local machine with 
    + `ctrl+shift+p`
    + Remote: Start Server

#### Set up at remote machine
- ssh into server and install rmate
```bash
ssh -v Rami
su
wget -O /usr/local/bin/rcode \
https://raw.github.com/aurora/rmate/master/rmate
chmod a+x /usr/local/bin/rcode

## Or, if do not have access to /usr/locl/bin/
wget -O ./rcode https://raw.github.com/aurora/rmate/master/rmate
chmod a+x ./rode

# set alias for rcode and put the following code at the end of ~/.bash_profile
alias code="rcode"
```


#### Usage

- use the rcode/code on server
```bash
code fileanme #note that it cannot be a folder
```