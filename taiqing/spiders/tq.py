# -*- coding: utf-8 -*-
import scrapy

from taiqing.items import TaiqingItem


class TqSpider(scrapy.Spider):
    name = 'tq'
    allowed_domains = ['tai-tech.com.tw']
    start_urls = ['https://www.tai-tech.com.tw/catalog?page=1']

    def parse(self, response):
        base_url = 'https://www.tai-tech.com.tw/'
        urls = response.xpath('//ul[@class ="list noneStyle clearfix"]/li/a/@href').extract()
        names = response.xpath('//h3/span/text()').extract()
        for url,name in zip(urls,names):
            new_url = base_url + url
            name = name.replace('/'," ")
            yield scrapy.Request(url=new_url,meta={'name':name},callback=self.seriesParse)

    def seriesParse(self,response):
        item=TaiqingItem()
        item['name']=response.meta['name'] #按应用分类的名字
        series = response.xpath('//div[@class="list"]')
        base_url = 'https://www.tai-tech.com.tw/'
        for s in series:
            seriesNames = series.xpath('./h3/text()').extract()
            pdfurls = series.xpath('./div')
            for url,name in zip(pdfurls,seriesNames):
                item['seriesName']=name.replace('/',' ')
                for durl in url.xpath('.//td[last()-2]//a/@href').extract():
                    item['pdfurl'] = base_url + durl
                    yield item
