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
    url = 'https://en.wikipedia.org/wiki/Index_of_agriculture_articles#A'
    response = requests.get(url)
    soup =BS(response.content,'lxml')
    #print(soup)
    body = soup.find('div',{"class" : "mw-parser-output"})
    #print(body)
    table = body.find('table', {"class" : "vertical-navbox nowraplinks"})
    table.extract()
    Indices_table = body.find_all('div',{"role" : "navigation"})
    #References = body.find('span',{"id" : "References"})
    #Portal = body.find('a',{"title" : "Portal:Contents/Indices"})
    list =[]
    if (Indices_table is not None):
        for i in Indices_table:
            i.extract()
    body = body.find_all("ul")
    for ul in body:
        indexes = ul.find_all("a")
        for text in indexes:
            list.append(text.get_text())
    for i in range(len(list)):
        print(list[i])
    