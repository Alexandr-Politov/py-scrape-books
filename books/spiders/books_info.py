import scrapy
from scrapy.http import Response


class BooksInfoSpider(scrapy.Spider):
    name = "books_info"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response: Response, **kwargs):
        pass
