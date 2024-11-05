import scrapy
from scrapy.http import Response


class BooksInfoSpider(scrapy.Spider):
    name = "books_info"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response: Response, **kwargs):
        for book in response.css(".product_pod"):
            yield {
                "link": book.css(".image_container a::attr(href)").get()
            }

        next_page = response.css(".pager .next a::attr(href)").get()
        if next_page:
            next_page_url = "https://books.toscrape.com/catalogue/" + next_page
            yield scrapy.Request(next_page_url, callback=self.parse)


    # title = response.css(".product_main > h1::text").get()
    # price = int(response.css(".price_color::text").get()[1:])
    # amount_in_stock = response.css(".instock.availability::text").re_first(r'\d+')
    # rating = response.css(".star-rating::attr(class)").re_first(r'\b(One|Two|Three|Four|Five)\b')
    # category = response.css(".breadcrumb li")[-2].css("a::text").get()
    # description = response.css("#product_description + p::text").get()
    # upc = response.css(".table.table-striped td::text").get()
