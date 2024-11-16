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


# configure bash
cd ~
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.profile

pyenv activate trimmer-python
pyenv virtualenvs


pip install --upgrade pip
pip install pip-tools
pip-sync
pip-compile --upgrade && pip-sync
pre-commit install
pre-commit run --all
```

Install dependencies:

```
pip3 install -r requirements.txt
```

and create link to `trimmer` file:

```
cd ~/bin
ln -s /path/to/the/repo/trimmer-python/main.py trimmer
```

I assume that `~/bin` directory is included in your `PATH`.

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
