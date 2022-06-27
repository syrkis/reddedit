#!/bin/bash
export PATH="~/.pyenv/bin:$PATH"
source reddedit/.env 


if ! command -v pyenv &> /dev/null
then # If no pyenv is found 
    echo "pyenv could not be found, cannot initialize env"
else
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
fi

#. /home/$USER/.bashrc

pyenv activate PYENV
cd reddedit/
python main.py data.csv &> out.log
