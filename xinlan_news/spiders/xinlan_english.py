# -*- coding: utf-8 -*-
import scrapy
from xinlan.items import XinlanItem

class XinlanEnglishSpider(scrapy.Spider):
    name = 'xinlan_english'
    allowed_domains = ['english.sina.com']
    start_urls = ['http://english.sina.com/news/china/']

    def parse(self, response):
        res = response.xpath('//body/script').re(r'<div class="r-info"><h4><a href="(.*)"')
        for i in res:
            result=i[0:71].replace('" t','')
            item=XinlanItem()
            item['news_url']=result

            request = scrapy.Request(url=item['news_url'],
                                     callback=self.parse_news)
            request.meta['item'] = item
            yield request

    def parse_news(self,response):
        # 获取子页简介信息
        item = response.meta['item']
        title = response.xpath('//div[@id="artibodyTitle"]//h1/text()').get()
        time=response.xpath('//div[@class="t_attr"]//span/text()').get()
        content=response.xpath('//div[@id="artibody"]//p/text()').getall()
        new_title = ''.join(title).strip()
        item['title']=new_title
        item['time']=time
        if content:
            new_content = ''.join(content).strip().replace("\"","")
        else:
            new_content='Null'
        item['content'] = new_content
        yield item



