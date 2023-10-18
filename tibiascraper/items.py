# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TibiascraperItem(scrapy.Item):
    # define the fields for your item here like:
    players_online = scrapy.Field()
    monster_day = scrapy.Field()
    boss_day = scrapy.Field()
    pass
