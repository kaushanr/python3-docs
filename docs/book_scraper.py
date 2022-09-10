
import scrapy

class BookSpider(scrapy.Spider):

  name = 'bookspider'  
  start_urls = ['http://books.toscrape.com/']

  def parse(self,response):
    for article in response.css('article.product_pod'): # looks at article tags with class = product-pod - css syntax
      yield {
          'price': article.css('.price_color::text').extract_first(),
          'title': article.css('h3 > a::attr(title)').extract_first() # CSS selector syntax used here...
      }
      next = response.css('.next > a::attr(href)').extract_first()
      if next:
        yield response.follow(next,self.parse) # recursion by calling the function internally again
