import scrapy
from zolpic.items import ZolpicItem
import os
import requests


def download_pic(url):
    first_name = url[-10:]
    path = os.getcwd()
    name = path + first_name.replace('/', '.')
    print('pathname:', name)
    if not os.path.exists(name):
        data = requests.get(url)
        with open(path + first_name, 'wb') as f:
            f.write(data.content)
        f.close()
    else:
        pass


class DeskSpider(scrapy.Spider):
    # 蜘蛛的名字不能重复
    name = 'desk'
    # 定义蜘蛛的采集范围
    allowed_domains = ['desk.zol.com.cn']
    # 定义开始爬取的地址
    start_urls = (
        'http://desk.zol.com.cn/1920x1080/'
    )

    def parse(self, response):
        url = response.xpath('//ul[@class="pic-list2  clearfix"]/li/a/@href').extract()
        for i in url:
            i = 'http://desk.zol.com.cn' + i
            yield scrapy.Request(url=i, callback=self.parse_url)

    def parse_url(self,response):
        imglist=response.xpath('')