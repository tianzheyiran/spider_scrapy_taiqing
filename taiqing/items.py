# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaiqingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapyProject.Field()
    name = scrapy.Field()
    pdfurl = scrapy.Field()
    seriesName = scrapy.Field()