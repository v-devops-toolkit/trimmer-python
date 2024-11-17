# trimmer

## Install

Clone the repo:

```
git clone git@github.com:gajdaw/trimmer-python.git
```

## pyenv

```
brew install pyenv-virtualenv
brew update && brew upgrade pyenv
pyenv install 3.12
pyenv virtualenvs
pyenv virtualenv 3.12 trimmer-python

pyenv activate trimmer-python
pyenv virtualenvs

pip install --upgrade pip
pip install pip-tools
pip-sync
```

Install dependencies:

```
pip install -r requirements.txt
```

and create bash file named `trimmer.sh` with the contents:

```
#!/bin/bash

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv activate trimmer-python
python3 /PATH/TO/YOUR/REPO/trimmer-python/main.py $*
```

Copy bash script `trimmer` to the directory which is included in your paths.

## Run

```
trimmer
trimmer right
trimmer right --dir=.
```

## Unit tests

Run:

```
pytest test*.py
```

or

```
python3 -m pytest test*.py
```
