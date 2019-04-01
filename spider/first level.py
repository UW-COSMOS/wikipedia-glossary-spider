# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:42:38 2019

@author: leo
"""
import requests
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from bs4 import BeautifulSoup as BS

class test:
    url = 'https://en.wikipedia.org/wiki/Category:Indexes_of_science_articles'
    response = requests.get(url)
    soup =BS(response.content,'lxml')
    soup = soup.select("ul li a")
    print(soup[26]['href'])
    for i in range(1,38):
        print(soup[i]['href'])
    bullet_index = [1,2,6,7,8,10,13,15,19,20,23,24,25,27,30,33,34,36,37]
    for i in bullet_index:
        print(i)
        