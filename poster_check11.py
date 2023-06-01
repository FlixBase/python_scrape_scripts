#!/usr/bin/env python

import json
import csv
import time
import pandas as pd
import re as re
import copy
adult=pd.read_csv("old/input_02.csv",encoding = 'unicode_escape',usecols=['adult'])
imdb_id=pd.read_csv("old/input_02.csv",encoding = 'utf-8',usecols=['imdb_id'])
release_date=pd.read_csv("old/input_02.csv",encoding = 'unicode_escape',usecols=['release_date'])
title=pd.read_csv("old/input_02.csv",encoding = 'utf-8',usecols=['title'])
description=pd.read_csv("old/input_02.csv",encoding = 'utf-8',usecols=['overview'])
vote_avg=pd.read_csv("old/input_02.csv",encoding = 'unicode_escape',usecols=['vote_average'])
vote_count=pd.read_csv("old/input_02.csv",encoding = 'unicode_escape',usecols=['vote_count'])
popularity=pd.read_csv("old/input_02.csv",encoding = 'unicode_escape',usecols=['popularity'])
poster_url=pd.read_csv("old/input_02.csv",encoding = 'unicode_escape',usecols=['poster_path'])
genre=pd.read_csv("old/input_02.csv",encoding = 'utf-8',usecols=['genres'])
csv_id=pd.read_csv("old/input_02.csv",usecols=['csv'])
text1="INSERT INTO movies (csv_id, imdb_id, title, description, release_date, adult, vote_avg, vote_count, popularity, poster_url,temp_genre) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$0,'hahaha');"
validity=pd.read_csv("old/input_02.csv",encoding = 'unicode_escape',usecols=['Valid'])
poster_url1=pd.read_csv("old/input_02.csv",encoding = 'unicode_escape',usecols=['poster_path1'])



adult=sum(adult.values.tolist(),[])
imdb_id=sum(imdb_id.values.tolist(),[])
release_date=sum(release_date.values.tolist(),[])
title=sum(title.values.tolist(),[])
description=sum(description.values.tolist(),[])
vote_avg=sum(vote_avg.values.tolist(),[])
vote_count=sum(vote_count.values.tolist(),[])
popularity=sum(popularity.values.tolist(),[])
poster_url=sum(poster_url.values.tolist(),[])
poster_url1=sum(poster_url1.values.tolist(),[])
genre=sum(genre.values.tolist(),[])
csv_id=sum(csv_id.values.tolist(),[])
validity=sum(validity.values.tolist(),[])

insert_txt="insertx.txt"
#temp=[{'id': 10749, 'name': 'Romance'}, {'id': 18, 'name': 'Drama'}, {'id': 80, 'name': 'Crime'}]
"""temp=[str(x).replace('{',"") for x in temp]
temp=[str(x).replace('}',", ") for x in temp]
temp="".join(temp)
temp=temp.replace(":",',')
temp=temp.split(', ')
r=[3,7,11,15,19,23]
temp=[x for x in temp if temp.index(x) in r]
temp="".join(temp)
temp=temp.replace("''",',')
print(temp)"""
r=[3,7,11,15,19,23,27]
digits=['1','2','3','4','5','6','7','8','9','0']
for i in range(len(validity)):
    if validity[i]==True:
        text=copy.deepcopy(text1)

        text=text.replace('$1',str(csv_id[i]))
        #csv_id
        text=text.replace('$2',"'"+imdb_id[i]+"'")
        temp=title[i]
        temp=temp.replace("'","''")
        text=text.replace('$3',"'"+temp+"'")
        temp=description[i]
        temp=(str(temp)).replace("'","''")
        text=text.replace('$4',"'"+str(temp)+"'")
        text=text.replace('$5',"'"+str(release_date[i])+"'")
        text=text.replace('$6',str(adult[i]))
        text=text.replace('$7',str(vote_avg[i]))
        text=text.replace('$8',str(vote_count[i]))
        text=text.replace('$9',str(popularity[i]))
        text=text.replace('$0',"'"+str(poster_url[i])+"'")
        temp=genre[i]
        temp=[str(x).replace('{',"") for x in temp]
        temp=[str(x).replace('}',", ") for x in temp]
        temp="".join(temp)
        temp=temp.replace(":",',')
        temp=temp.split(', ')
        temps=[]
        for n in range(len(temp)):
            if n==3:
                temps.append(temp[n])
            if n==8:
                temps.append(temp[n])
            if n==13:
                temps.append(temp[n])
            if n==18:
                temps.append(temp[n])
            if n==23:
                temps.append(temp[n])
            if n==28:
                temps.append(temp[n])
            if n==33:
                temps.append(temp[n])
        temp=",".join(temps)
        temp=temp.replace("'",'')
        if len(temp)>0:
            text=text.replace('hahaha',temp) 
            with open(insert_txt, "a") as myfile:
                 myfile.write(text+ "\n")


