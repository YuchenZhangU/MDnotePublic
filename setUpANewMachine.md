## dotfiles

```bash
git clone https://github.com/YuchenZhangU/dotfiles.git

# .bashrc
source ~/dotfiles/.bashrc

# git
[include]
    path = ~/dotfiles/.gitconfig

# vim
source ~/dotfiles/.vimrc

# tmux
source ~/.tmux.conf


# Or if it is a new machine use install.sh to install
chmod a+x ./install.sh
./install.sh
```

## vscode setup

install extension `Settings Sync` by Shan Khan
 
use command `Sync:Update/Upload Settings` to input github token and gist id

GitHub Token: d75f59002ecb4331378a46666158d020d9468b23

`"sync.gist": "2b8054ce57f81c1cfa7e10cc42a92075",`

GitHub Gist: 2b8054ce57f81c1cfa7e10cc42a92075


## install tmux

```bash
sudo apt-get install tmux
# or 
sudo yum install tmux
```

## ssh setting 

### ssh key

under local machine `$HOME/.ssh/`

```bash
ssh-keygen -t rsa -C "key generated for xxx"
# will get `id_rsa.pub` and `id_rsa`, id_rsa.pub will be put into remote machine


# move authorized pub key to remote machine
scp $HOME/.ssh/id_rsa.pub user@server1.cyberciti.biz:~/.ssh/authorized_keys
```

### shortcut

## Rcode

1. install remote-vscode
`ext install remote-vscode`

2. set ssh Remote Forward

Put the following code in ~/.ssh/config
```
Host myRemoteServerName
    HostName 12.34.567.89
    User root
    ForwardAgent yes
    RemoteForward 52698 127.0.0.1:52698
```

ssh -v myRemoteServerName

3. 

sudo wget -O /usr/local/bin/rcode \
https://raw.github.com/aurora/rmate/master/rmate
chmod a+x /usr/local/bin/rcode
