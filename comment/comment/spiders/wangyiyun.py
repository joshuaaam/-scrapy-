import scrapy
from selenium import webdriver
import pymysql
import time

class WangyiyunSpider(scrapy.Spider):
    name = 'wangyiyun'
    allowed_domains = ['https://music.163.com']


    def start_requests(self):
        # 循环歌手
        # 跳转循环歌曲进入

        yield scrapy.Request(url="https://music.163.com/#/discover/artist/cat",callback=self.get_singer_list,dont_filter=True)
        # self.browser.get("https://music.163.com/#/discover/artist/cat?id=1001")
        # iframe_elemnt = self.browser.find_element_by_id("g_iframe")
        # self.browser.switch_to.frame(iframe_elemnt)
        # elements = self.browser.find_elements_by_xpath("//ul[@id='initial-selector']/li/a")
        # elements = self.browser.find_elements_by_xpath("//div[@class='m-sgerlist']/ul/li")


    #
    def get_singer_list(self,response):
        print(response)
        # url = response.meta['url']
        # print('1',url)
        # self.browser.get(url)
        #
        # iframe_elemnta = self.browser.find_element_by_id("g_iframe")
        # self.browser.switch_to.frame(iframe_elemnta)
        #
        # elements = self.browser.find_elements_by_xpath("//div[@class='m-sgerlist']/ul/li[@class='sml']/a[1]")
        # for item in elements:
        #     href = item.get_attribute('href')
            # print(href)

            # yield scrapy.Request(url=href, callback=self.get_song_list,meta={'href':href}, dont_filter=True)
            # self.get_song_list(href)

    def get_song_list(self,response):
        href = response.meta['href']
        print('1', href)
        self.browser.get(href)
    #