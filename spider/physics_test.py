# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:59:12 2019

@author: leo
"""

import requests
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from bs4 import BeautifulSoup as BS

class test:
    url = 'https://en.wikipedia.org/wiki/Index_of_sociology_articles'
    response = requests.get(url)
    soup =BS(response.content,'lxml')
    #print(soup)
    body = soup.find('div',{"class" : "mw-parser-output"})
    #print(body)
    table = body.find('table', {"class" : "vertical-navbox nowraplinks"})
    if (table is not None):
            table.extract()
    Indices_table = body.find_all('div',{"role" : "navigation"})
    if (Indices_table is not None):
        for i in Indices_table:
            i.extract()
    toc = body.find('div', {"id": "toc"})
    if (toc is not None):
        toc.extract()
    contents = []
    for i in body.find_all('h2'):
        p = i.find_next_sibling('p')
        if (p is not None):
            indexes = p.find_all('a')
            for index in indexes:
                contents.append(index.get_text())
    print(contents)