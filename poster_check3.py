#!/usr/bin/env python

import json
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import re as re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

df=pd.read_csv("input_0.csv")#usecols=['poster_path'])
df1=pd.read_csv("input_0.csv",usecols=['poster_path'])


poster=df1.values.tolist()
poster=sum(poster,[]) 


basic_url="https://image.tmdb.org/t/p/original"
#https://image.tmdb.org/t/p/original/6ksm1sjKMFLbO7UY2i6G1ju9SML.jpg
checked=[]
values=[]
browser = webdriver.Chrome(options=Options(),service=Service(ChromeDriverManager().install()))
#a=browser.page_source
c=0

for i in range(len(poster)):
    links=str(basic_url)+str(poster[i])
    browser.get(links)
    a=browser.page_source
    a=a.split("title>")
    if a[1].startswith("File Not Found"):
        checked.append(links)
        values.append(False)
    else: 
        checked.append(str(poster[i]))
        values.append(True)
        c+=1
browser.close()
columns1=['poster_path','Valid']
a=pd.DataFrame(list(zip(checked,values)),columns=columns1)
file_csv="validation_inp_0.csv"
a.to_csv(file_csv, columns =columns1)
