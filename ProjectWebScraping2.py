from os import write
from bs4 import BeautifulSoup as bs
import time,csv
import pandas as pd
import csv
from selenium import webdriver as wd
import requests
from urllib3 import request

# opening the link of nasa webpage
startUrl='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser=requests.get(startUrl)

temp_list=[]


soup=bs(browser.text,'html.parser')
star_table=soup.find_all('table')
print(len(star_table))
table_rows=star_table[4].find_all('tr')

for trtag in table_rows:
    tdtags=trtag.find_all('td')

    row=[i.text.rstrip()for i in tdtags]

    temp_list.append(row)

star_names=[]
star_dist=[]
star_mass=[]
star_rad=[]

for i in range(1,(len(temp_list))):
    star_names.append(temp_list[i][0])
    star_dist.append(temp_list[i][5])
    star_mass.append(temp_list[i][8])
    star_rad.append(temp_list[i][9])

df2=pd.DataFrame(list(zip(star_names,star_dist,star_mass,star_rad)),columns=['Names','Distance','Mass','Radius'])
df2.to_csv('ProjectScrapedData.csv')
print(temp_list)