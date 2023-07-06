import scrapy
from pymongo import MongoClient

class KitapsepetiSpider(scrapy.Spider):
    name = "kitapsepeti"
    start_urls = [
        'https://www.kitapsepeti.com/roman',
    ]

    custom_settings = {
        'FEEDS': {
            'books.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'indent': 4,
                'overwrite': True,
            },
        },
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DOWNLOAD_DELAY': 5,  
    }

    def parse(self, response):
        for book in response.css('div.box'):
            title = book.css('a.text-description::text').get()
            publisher = book.css('a.col.text-title::text').get()
            author = book.css('a#productModelText::text').get()
            price = book.css('div.col.currentPrice::text').get()
            if price:
                price = price.strip()

            yield {
                'title': title.strip() if title else "",
                'publisher': publisher.strip() if publisher else "",
                'author': author.strip() if author else "",
                'price': price.strip() if price else ""
            }

        next_page = response.css('//div[@class="productPager"]/a[@title="İleri"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)
 

    def closed(self, reason):
        client = MongoClient('mongodb://localhost:27017')
        db = client['smartmaple']
        collection = db['kitapsepeti']

        data = list(collection.find())
        print(data)
        client.close()



