#!/bin/bash


/home/ubuntu/py35/bin/activate

wget https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/$1.csv

python load.py $1.csv
python usload.py $1.csv
