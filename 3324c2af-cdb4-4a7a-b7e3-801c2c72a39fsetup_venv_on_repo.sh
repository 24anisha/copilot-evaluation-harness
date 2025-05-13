#!/bin/bash
set -xe
if [ ! -d 'out/repos/maurosoria/dirsearch/maurosoria--dirsearch/.venv' ]; then python3 -m venv 'out/repos/maurosoria/dirsearch/maurosoria--dirsearch/.venv'; fi
source out/repos/maurosoria/dirsearch/maurosoria--dirsearch/.venv/bin/activate
python3 -m pip install -r 'out/repos/maurosoria/dirsearch/maurosoria--dirsearch/requirements.txt' > /dev/null