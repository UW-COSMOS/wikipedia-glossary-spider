# -*- coding: utf-8 -*-
import scrapy
import requests
from scientific.items import ScientificItem
from scrapy.http import Request
from bs4 import BeautifulSoup as BS


class ScientificIndexesSpider(scrapy.Spider):
    name = 'scientific_indexes'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Category:Indexes_of_science_articles']
    

    def parse(self, response):
        #category_list = response.xpath('//*[@id="mw-pages"]/div/div')
        #item['subject_url'] = 'https://en.wikipedia.org/wiki/Index_of_agriculture_articles#A'
        #for category in category_list:
        #    subjects = category.xpath('./ul')
        #    for subject in subjects:
        #       item['subject_url'] = category.xpath('./a/@href').extract()[0]
        soup =BS(response.text,'lxml')
        soup = soup.select("ul li a")
        bullet_index = [1,2,6,7,8,10,13,15,19,20,23,24,25,27,29,30,33,34,36,37]
        for i in range(1,38):
            item = ScientificItem();
            item['subject_url'] = 'https://' +  self.allowed_domains[0] + soup[i]['href']
            if(i == 26): #physics
                yield  Request(item['subject_url'], meta = {'item':item}, callback = self.parse_subject_physics, dont_filter =True)
            elif(i in bullet_index):
                yield  Request(item['subject_url'], meta = {'item':item}, callback = self.parse_subject_bullet, dont_filter =True)
            else:
                yield  Request(item['subject_url'], meta = {'item':item}, callback = self.parse_subject_hyphen, dont_filter =True)
    def parse_subject_bullet(self, response):
        item = response.meta['item']
        item['subject_name'] = response.xpath('//*[@id="firstHeading"]//text()').extract()[0]
        #html = requests.get(response.url)
        #soup = BeautifulSoup(html.content, 'lxml')
        soup =BS(response.text,'lxml')
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
        #References = body.find('span',{"id" : "References"})
        #Portal = body.find('a',{"title" : "Portal:Contents/Indices"})
        body = body.find_all("ul")
        item['subject_indexes'] = []
        for ul in body:
            indexes = ul.find_all("a")
            for text in indexes:
                item['subject_indexes'].append(text.get_text())
        yield item
        
    def parse_subject_physics(self, response):
        item = response.meta['item']
        item['subject_name'] = response.xpath('//*[@id="firstHeading"]//text()').extract()[0]
        content = response.xpath('//*[@id="toc"]/ul')
        for li in content.xpath('//li'):
            url = 'https://' +  self.allowed_domains[0] + li.xpath('./a/@href').extract()[0]
            yield Request(url, meta = {'item':item}, callback = self.parse_subject_physics_index, dont_filter =True)
        
    
    
    def parse_subject_physics_index(self, response):
        item = response.meta['item']
        soup =BS(response.text,'lxml')
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
        #References = body.find('span',{"id" : "References"})
        #Portal = body.find('a',{"title" : "Portal:Contents/Indices"})
        body = body.find_all("ul")
        item['subject_indexes'] = []
        for ul in body:
            indexes = ul.find_all("a")
            for text in indexes:
                item['subject_indexes'].append(text.get_text())
        yield item
        
        
    def parse_subject_hyphen(self, response):
        item = response.meta['item']
        item['subject_name'] = response.xpath('//*[@id="firstHeading"]//text()').extract()[0]
        #html = requests.get(response.url)
        #soup = BeautifulSoup(html.content, 'lxml')
        soup =BS(response.text,'lxml')
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
        item['subject_indexes'] = []
        for i in body.find_all('h2'):
            p = i.find_next_sibling('p')
            if (p is not None):
                indexes = p.find_all('a')
                for index in indexes:
                    item['subject_indexes'].append(index.get_text())
        yield item
        
        
        
        
            
