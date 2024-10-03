
import scrapy
from scrapy.crawler import CrawlerProcess
import json

class SEOSpider(scrapy.Spider):
    name = 'seo_spider'
    
    def __init__(self, start_url=None, *args, **kwargs):
        super(SEOSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url] if start_url else []

    def parse(self, response):
        # Extract meta title
        title = response.css('title::text').get()
        
        # Extract meta description
        description = response.xpath("//meta[@name='description']/@content").get()
        
       #need a way to look at more keywords 
        
        # Extract other relevant meta tags
        og_title = response.xpath("//meta[@property='og:title']/@content").get()
        og_description = response.xpath("//meta[@property='og:description']/@content").get()
        
        item = {
            'url': response.url,
            'title': title,
            'description': description,
            'og_title': og_title,
            'og_description': og_description,
        }
        
        print(json.dumps(item, indent=2))  # Print the scraped data
        yield item

def run_spider(url):
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'LOG_LEVEL': 'ERROR'
    })

    process.crawl(SEOSpider, start_url=url)
    process.start()

if __name__ == "__main__":
    target_url = input("Enter the URL to scrape: ")  
    run_spider(target_url)
