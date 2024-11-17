#!/bin/bash

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv activate trimmer-python 2>/dev/null
python3 /PATH/TO/YOUR/REPO/trimmer-python/main.py $*
