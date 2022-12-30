import scrapy
import csv
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class MajesticSpider(scrapy.Spider):
    name = "majestic"
    domains = []
    #open top 1m majestic sites
    with open(r'D:\Project\Web-Based-Cryptojacking-Scanner\site-lists\majestic_million.csv', 'r', encoding='utf-8') as csv_file:
       reader = csv.reader(csv_file)
       for i, row in enumerate(reader):
            if i == 0: continue #skip header row in the csv file
            domains.append('https://' + row[2])
            #break
    start_urls = domains #['http://aahora.org']
    rules = (
        Rule(LinkExtractor(), callback='parse', follow=True),
    )
   
    def parse(self, response):
        keywords = ['_client.start', 'coinhive.min.js', 'CoinHive.Anonymous', 'load.jsecoin.com', 'CRLT.Anonymous(', 'WMP.Anonymous(', 'bmst.pw', 'wp-monero-miner', 'nerohut.com/srv', 'webmr.js', 'cdn.minescripts.info', 'deepMiner.Anonymous', 'monerise_payment_address', 'webmine.cz', 'CoinNebula', 'authedmine.min.js', 'simple-ui.min.js', 'authedmine.eu/lib/1.js']
        for script in response.css("script").extract():
            js_script = str(script)
            for keyword in keywords:
                if keyword in js_script:
                    yield {'site': str(response).split(' ')[-1], 'script_found': script, 'keyword': keyword}
                else:
                    pass
            
