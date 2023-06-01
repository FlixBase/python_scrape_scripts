#!/usr/bin/env python
"""This script is used to add scraped from imdb reviews to db"""
import json
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
from time import sleep
import pandas as pd
import re as re
import math
import copy
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#print(rows1)
#$4=star
#$3=review
#$1=username
#$2=username+@example.com'
#$5=imdb_id

text="WITH inserted_user AS (INSERT INTO users (username, password, email) VALUES ($1, '1', $2) RETURNING id), reviewed_movie AS (select * FROM movies where imdb_id=$5) INSERT INTO views (user_id, movie_id, review, favorite, rating) SELECT inserted_user.id, reviewed_movie.id, $3, false, $4 FROM inserted_user, reviewed_movie;"
imdb_id=pd.read_csv("input11.csv",encoding="utf-8",usecols=['imdb_id'])
df=pd.read_csv("input11.csv",encoding="utf-8",usecols=['title'])
csv_id=pd.read_csv("input11.csv",encoding="utf-8",usecols=['csv_id'])

imdb_id=imdb_id.values.tolist()
title=df.values.tolist()
imdb_id=sum(imdb_id,[])
title=sum(title,[])

base_page_url="https://www.imdb.com/title/" #tt0114709/reviews"
#
file_csv="reviews_whole/whole_"

browser = webdriver.Chrome(options=Options(),service=Service(ChromeDriverManager().install()))
for i in range(len(imdb_id)):
    page_url=base_page_url+imdb_id[i]+"/reviews"
    browser.get(page_url)
    a=browser.page_source
    #sleep(1)
    file_csv1=file_csv+imdb_id[i]+"_.txt"
    text_file=open(file_csv1, "w")
    text_file.write(a)
    text_file.close()
usernames=[]
insert="reviews_whole/insert_reviews.txt"
reviews_txt="reviews_whole/reviews_"
for j in range(len(imdb_id)):
    file_csv1=file_csv+imdb_id[j]+"_.txt"
    with open(file_csv1, 'r') as f:
        lines=f.readlines();
    for i in range(len(lines)):
        if lines[i].startswith('                <div class="text show-more__control'):
            text1=copy.deepcopy(text)
            temp=lines[i].replace('                <div class="text show-more__control','')
            temp=temp.replace('<br>','')
            temp=temp.replace('</div>','')
            temp=temp.replace('">','')
            temp=temp.replace(' clickable','')
            temp=temp.replace("'","''")
            text1=text1.replace('$3',"'"+temp+"'")
            with open(reviews_txt+imdb_id[j]+"_.csv", "a") as myfile:
                myfile.write(temp+ "\n")
            text1=text1.replace('$5',"'"+imdb_id[j]+"'")
            temp1=lines[i-3]
            if '<span class="display-name-link">' in temp1:
                temp1=temp1.split('</a></span><span class="review-date">')
                temp1=temp1[0]
                temp1=temp1.split('>')
            else:
                temp1='N'
            temp1=temp1[-1]
            if temp1 in usernames:
                usernames.append(temp1)
                c=usernames.count(temp1)-1
                temp1=temp1+str(c)
            else:
                usernames.append(temp1)
            text1=text1.replace('$1',"'"+temp1+"'")
            text1=text1.replace('$2',"'"+temp1+'@example.com'+"'")
            temp2=lines[i+38]
            if '</span><span' in temp2:
                temp2=temp2.replace('</span><span class="point-scale">','')
                temp2=temp2.replace('</span>','')
                temp2=temp2.replace('<span>','')
                temp2=temp2.replace(' ','')
            else:
                temp2='9/10'
            temp2=temp2.split('/')
            temp2=math.ceil(int(temp2[0])*0.5)
            text1=text1.replace('$4',str(temp2))
            with open(insert, "a") as myfile:
                myfile.write(text1+ "\n")

