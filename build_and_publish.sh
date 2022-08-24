#!/bin/sh

sudo apt-get install -y texlive texlive-latex-extra pandoc texlive-xetex

pip install -r requirements.txt

python -m icmlcrawler

