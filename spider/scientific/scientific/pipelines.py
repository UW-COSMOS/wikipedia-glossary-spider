# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
import os
import csv

class ScientificPipeline(object):
    def __init__(self):
        self.subjects_to_csv = {}
        self.file_names = {}
        pass
        

    def process_item(self, item, spider):
        subject = item['subject_name'].replace(' ', '_')
        store_file = os.path.dirname(__file__) + '/spiders/'
        if subject not in self.subjects_to_csv:
            file_name = store_file + subject + '.csv'
            self.file_names[subject] = file_name
            f = open(file_name, 'a', newline = '', encoding='utf-8')
        f = open(self.file_names[subject], 'a', newline = '', encoding='utf-8')
        writer = csv.writer(f, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(item['subject_indexes'])):
            writer.writerow([item['subject_indexes'][i]])
        f.close()
        return item
    

