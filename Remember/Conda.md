maintain

```bash
# update conda
conda update conda
conda update anaconda

# remove conda
rm -rf ~/anaconda2/
```


Create and activate, remove environment
```bash
# anaconda is the metapackage
conda create -n p3.7 python=3.7 anaconda

source active p3.7

# remove environment
conda remove --name myenv --all

# clone environment
conda create --name <env_name> --clone base

```

Update python version

```bash
conda update conda
conda install python=3.7
```


Info

```bash
# see current environment
conda info --envs
conda env list

# do not show environment name before prompt
conda config --set changeps1 false

# list packages in an environment
conda list -n myenv
conda list
```

