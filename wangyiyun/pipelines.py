# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WangyiyunPipeline(object):
    def process_item(self, item, spider):
        with open('wangyimiusc.csv', 'w+') as  f:
            f.write(item)
        return item
