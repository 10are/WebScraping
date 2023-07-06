import scrapy
import time

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
        'DOWNLOAD_DELAY': 1,  # İstekler arasında 1 saniye bekleme süresi
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

        next_page = response.css('.pagination a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse)

    def _crawl(self, *args, **kwargs):
        while True:
            self.crawler.engine.schedule(
                scrapy.Request(self.start_urls[0], callback=self.parse),
                self
            )
            time.sleep(60)

    def spider_idle(self):
        self._crawl()