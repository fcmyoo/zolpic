import scrapy
from zolpic.items import ZolpicItem
import os
import requests as rq

next_page_link = []
down_href_url = []
down_url = []


def download_pic(url, title='other'):
    first_name = url[-15:]
    path = os.getcwd()
    name = path + '\\pic' + '\\' + title + '\\' + first_name.replace('/', '.')
    print('pathname:', name)

    if not os.path.exists('pic\\' + title):
        os.makedirs('pic\\' + title)
        if not os.path.exists(name):
            data = rq.get(url)
            with open(name, 'wb') as f:
                f.write(data.content)
            f.close()
        else:
            pass
    else:
        if not os.path.exists(name):
            data = rq.get(url)
            with open(name, 'wb') as f:
                f.write(data.content)
            f.close()
        else:
            pass


class DeskSpider(scrapy.Spider):
    # 蜘蛛的名字不能重复
    name = 'desk'
    # 定义蜘蛛的采集范围
    allowed_domains = ['zol.com.cn']
    # 定义开始爬取的地址
    start_urls = ['http://desk.zol.com.cn/1920x1200/']

    def parse(self, response):
        rel_url = response.xpath('//ul[@class="pic-list2  clearfix"]/li/a/@href').extract()
        for herf in rel_url:
            newherf = 'http://desk.zol.com.cn%s' % herf
            yield scrapy.Request(url=newherf, callback=self.get_zol_url)
        page_url = response.xpath('//div[@class="page"]/a/@href').extract()[-1]
        page_url = 'http://desk.zol.com.cn%s' % page_url
        if page_url not in next_page_link:
            next_page_link.append(page_url)
            print('nexturl:', next_page_link)
            yield scrapy.Request(url=page_url, callback=self.parse)

    def get_zol_url(self, response):
        item = ZolpicItem()
        det_url = response.xpath("//*[@id='tagfbl']/a/@href").extract()[1]
        det_url = 'http://desk.zol.com.cn%s' % det_url
        if det_url not in down_url:
            down_url.append(det_url)
            yield scrapy.Request(url=det_url, callback=self.get_det_pic)
        item['title'] = response.xpath("//title/text()").extract()[0].split('-')[0]
        yield item
        one_down_url = response.xpath("//a[@id='pageNext']/@href").extract()
        one_down_url = 'http://desk.zol.com.cn%s' % one_down_url
        if one_down_url not in down_href_url:
            down_href_url.append(one_down_url)
            yield scrapy.Request(url=one_down_url, callback=self.get_zol_url)

    def get_det_pic(self, response):
        item = ZolpicItem()
        item['img'] = response.xpath('//img[1]/@src').extract()
        download_pic(item['img'], item['title'])
