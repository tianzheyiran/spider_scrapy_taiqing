# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline

class DownloadPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        pdfurl = item['pdfurl']
        seriesName = item['seriesName']
        name = item['name']

        yield Request(url=pdfurl,meta={'seriesName':seriesName,'name':name})

    def file_path(self, request, response=None, info=None):
        name = request.meta['name']
        seriesName = request.meta['seriesName']
        fileName = request.url.split('/')[-1]
        filePath = name + "/"+ seriesName +'/'+fileName
        return filePath
