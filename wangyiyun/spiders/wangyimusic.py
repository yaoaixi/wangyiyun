# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from wangyiyun.items import WangyiyunItem

class WangyimusicSpider(scrapy.Spider):
    name = "wangyimusic"
    allowed_domains = ["http://music.163.com/#/discove"]
    # 可以在这里改变爬取"歌单的页数", 本人只设置了一页
    start_urls = ['http://http://music.163.com/#/discove/']

    def parse(self, response):
        # 歌单的列表
        muisc_lists = response.xpath('.//li/div[@class="u-cover u-cover-1"]/a/@href').extract()
        for muisc_list in muisc_lists:
            yield Request(muisc_list,self.parsemusics, dont_filter=True)

    def parsemusics(self, response):
        # 获取首歌曲的url
        muisc_urls = response.xpath('.//table[@class="m-table "]/tbody//tr//span[@class="txt"]/a/@href').extract()
        for muisc_url in muisc_urls:
            # 进入歌曲的页面
            yield Request(muisc_url, dont_filter=True)

    def parsemusic(self, response):
        item = WangyiyunItem()
        # 获取歌曲名
        names = response.xpath('.//div[@class="tit"]/em[@class="f-ff2"]/text()').extract()[0]
        # 获取评论数量
        comments = response.xpath('.//span[@id="cnt_comment_count"]/text()').extract()[0]
        if comments > 10000:
            item['name'] = names
            item['comment'] = comments
        yield item
