import scrapy
from xici.items import XiciItem

class mySpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/']

    def parse(self, response):
        hosts = response.xpath("//tr/td[2]/text()")[1:].extract()
        ports = response.xpath("//tr/td[3]/text()")[1:].extract()
        addrs = response.xpath("//tr/td[4]/a/text()")[1:].extract()
        ip_types = response.xpath("//tr/td[6]/text()")[1:].extract()
        speeds = response.xpath("//tr/td[7]/div/@title")[1:].extract()
        connects = response.xpath("//tr/td[8]/div/@title")[1:].extract()
        exitses = response.xpath("//tr/td[9]/text()")[1:].extract()
        verifies = response.xpath("//tr/td[10]/text()")[1:].extract()
        ip_list = list(zip(hosts,ports,addrs,ip_types,speeds,connects,exitses,verifies))
        for ip in ip_list:
            item = XiciItem()
            item['host'] = ip[0]
            item['port'] = ip[1]
            item['addr'] = ip[2]
            item['ip_type'] = ip[3]
            item['speed'] = ip[4]
            item['connect'] = ip[5]
            item['exits'] = ip[6]
            item['verify'] = ip[7]
            yield item



