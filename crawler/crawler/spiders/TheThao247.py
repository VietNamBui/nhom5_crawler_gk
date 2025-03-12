import scrapy
from crawler.items import CrawlerItem


class Thethao247Spider(scrapy.Spider):
    name = "TheThao247"
    allowed_domains = ["thethao247.vn"]
    start_urls = ["https://thethao247.vn/"]

    def parse(self, response):
        matches = response.xpath("//div[@class='content']//li/a")

        for match in matches:
            item = CrawlerItem()

            item['title']  = match.xpath("@title").get()

            new_details_url = match.xpath("@href").get()
            if new_details_url:
                new_details_url = response.urljoin(new_details_url)
                yield scrapy.Request(url=new_details_url, callback=self.parse_matches, meta={'item': item})

    def parse_matches(self, response):
        item = response.meta['item']

        item['author'] = response.xpath(".//a[@class = 'post-time']/strong/text()").get()
        item['time'] = response.xpath(".//div[@class = 'time']/div/text()").get()
        item['area'] = response.xpath("//div[contains(@class, 'breadcrumb mb')]//a[@class = 'active']/@title").get()
        item['content'] = response.xpath("//div[contains(@class, 'txt_content')]//p[@class='sapo_detail']/text()").get()
        item['content'] = item['content'].replace('\r', '').replace('\n', '').replace('\t', '').strip()


        yield item

        
