# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:09:00 2019

@author: leo
"""

import requests
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from bs4 import BeautifulSoup as BS

class test:
    url = 'https://en.wikipedia.org/wiki/Index_of_psychology_articles'
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
    body.prettify()
    h2 = body.select('h2')
    start = h2[0]
    end = h2[-1]
    start_index = body.findChildren().index(start)
    end_index = body.findChildren().index(end)
    print(body.findChildren()[end_index].next_sibling)
    section = body.findChildren()[start_index:end_index+1]
    count = 0
    for i in section:
        i_str = i.prettify()
        i_soup = BS(i_str,'lxml')
        p = i_soup.find("p")
        if (p is not None):
            As = p.find_all("a")
            for a in As:
                count = count + 1
                if (count == 1):
                    print(a.get_text())
    print(count)
    