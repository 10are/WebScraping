import scrapy
from pymongo import MongoClient

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = [
        'https://www.kitapyurdu.com/index.php?route=product/category/&filter_category_all=true&category_id=64&sort=purchased_365&order=DESC&filter_in_stock=1',
    ]

    custom_settings = {
        'FEEDS': {
            'books.json': {'format': 'json'},
        }
    }

    def parse(self, response):
        for book in response.css('div.product-cr'):
            title = book.css('div.name.ellipsis a > span::text').get()
            if not title:
                title = book.css('div.name.ellipsis a::attr(title)').get()

            publisher = book.css('div.publisher span a span::text').get()

            price = book.css('div.price span.value::text').get()

            author = book.css('div.author.compact.ellipsis a::text').get()

            yield {
                'title': title.strip() if title else None,
                'publisher': publisher.strip() if publisher else None,
                'price': price.strip() if price else None,
                'author': author.strip() if author else None
            }

        next_page = response.css('.pagination .next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def closed(self, reason):
        client = MongoClient('mongodb://localhost:27017')
        db = client['smartmaple']
        collection = db['kitapyurdu']
        # MongoDB'ye kaydedilen verileri alın
        data = list(collection.find())
        print(data)
        client.close()
