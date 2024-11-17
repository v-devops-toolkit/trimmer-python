#!/bin/bash

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv activate trimmer-python
python3 /Users/gajdaw/github/v-devops-toolkit/trimmer-python/main.py $*
