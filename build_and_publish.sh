#!/bin/sh

sudo apt-get install -y texlive texlive-latex-extra pandoc texlive-xetex

pip install -r requirements.txt

python -m icmlcrawler
jupyter nbconvert --execute report/report.ipynb
jupyter nbconvert --to pdf report/report.ipynb
jupyter nbconvert --to markdown report/report.ipynb --output-dir='.' --output README.md
jupyter nbconvert --clear-output --inplace report/report.ipynb

# create a zip file to upload to github

rm data.zip
zip -r data.zip data/records.csv data/records.json "report/Leading Institutions.csv" report/report.ipynb report/report.pdf

