import scrapy
from tibiascraper.items import TibiascraperItem



class TibiaSpider(scrapy.Spider):
    name = 'tibiascraper'
    start_urls = [
        'https://www.tibia.com/community/?subtopic=worlds' 
    ]

    def parse(self, response):  
        
       
        worlds = response.css('tr.Even, tr.Odd')
        for world in worlds:
            name = world.css('td a::text').get()
            boss_day =
            monster_day = 
            players_online = world.css('td:nth-child(2)::text').get()
            yield {
                'world': name.strip() if name else name,
                'players_online': int(players_online.strip()) if players_online else 0,
            }


    
        