# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
#import csv
import json
import random
import requests
temp=[]


#url =f"https://xkcd.com/{page}"
url =f"http://meisu.huaban.com/goods.php?media_id=117560362"
print(url)
data= requests.get(url)
final = []
bs = BeautifulSoup(data.text, "html.parser")  # 创建BeautifulSoup对象
body = bs.body

divone = body.find('div', {'class': 'picture_info'})
divtwo = divone.find('div', {'class': 'picture_head picture_head02'})
divthree = divtwo.find('div', {'class': 'wrapper'})
divfour = divthree.find('div', {'class': 'img'})

img = divfour.find('img')
imgelink = img['src']

# jdurl=jd['src']
final.append(imgelink)
temp.append(final)
print(final)
  
