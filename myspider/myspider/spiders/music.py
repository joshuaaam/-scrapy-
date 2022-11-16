import scrapy
from selenium import webdriver
import pymysql
import time
# browser = webdriver.Chrome('/usr/local/bin/chromedriSver')
# #
# browser.get("https://music.163.com/#/discover/toplist?id=19723756")
#
# conn = pymysql.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="19970913",
#     database="joshua",
#     charset="utf8mb4"
# )
# cursor = conn.cursor()
# sql = 'insert into comments (content,m_name,auto_name,singer,create_at,mid,auto_avatar) values (%s,%s,%s,%s,%s,%s,%s);'
# arr = []
#
#
# while True:
#     # 切换到iframe中
#     # 获取 iframe 对象
#     iframe_elemnt = browser.find_element_by_id("g_iframe")
#     browser.switch_to.frame(iframe_elemnt)
#     elements = browser.find_elements_by_xpath('//tr/td[2]/div[@class="f-cb"]/div[@class="tt"]/div[@class="ttc"]/span[@class="txt"]/a')
#     for item in elements:
#         href = item.get_attribute('href')
#         arr.append(href)
#         print(arr)
#     for urlitem in arr:
#         # if(urlitem)
#         browser.get(urlitem)
#         iframe_elemnta = browser.find_element_by_id("g_iframe")
#         browser.switch_to.frame(iframe_elemnta)
#         browser.implicitly_wait(5)  # 显式等待1秒
#         m_name = browser.find_element_by_xpath('//div[@class="tit"]/em').text
#         c_name = browser.find_element_by_xpath('//p[@class="des s-fc4"]/span/a').text
#
#         elementss = browser.find_elements_by_xpath('//*[@class="m-cmmt"]/div[2]/div/div[2]/div[1]/div')
#         for items in elementss:
#             index = items.text.index('：') + 1
#             auto = items.text[:index-1]
#             comment = items.text[index:]  # 解析评论
#             print(auto,comment[1:-1])
#             cursor.execute(sql, [comment, m_name,auto,c_name])
#         conn.commit()
#
#
#
# # 关闭连接
# cursor.close()
# conn.close()
# browser.quit()

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get("https://music.163.com/#/artist?id=7219")

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="19970913",
    database="joshua",
    charset="utf8mb4"
)
cursor = conn.cursor()
sql = 'insert into comments (content,music_name,singer,auto_name,img,comment_createtime,album,create_at,mid,auto_avatar,likes) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
arr = []

while True:
    iframe_elemnt = browser.find_element_by_id("g_iframe")
    browser.switch_to.frame(iframe_elemnt)
    elements = browser.find_elements_by_xpath('//tr/td[2]/div[@class="f-cb"]/div[@class="tt"]/div[@class="ttc"]/span[@class="txt"]/a')
    for item in elements:
        href = item.get_attribute('href')
        arr.append(href)
        print(arr)
    for urlitem in arr:
        browser.get(urlitem)
        iframe_elemnta = browser.find_element_by_id("g_iframe")
        browser.switch_to.frame(iframe_elemnta)
        browser.implicitly_wait(3)  # 显式等待1秒

        mid=7219
        # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        img = browser.find_element_by_xpath('//div[@class="m-lycifo"]/div[1]/div[1]/div/img').get_attribute("src")
        print(img)

        music_name = browser.find_element_by_xpath('//div[@class="tit"]/em').text
        singer = browser.find_element_by_xpath('//div[@class="cnt"]/p[1]/span/a').text
        print(singer)
        album = browser.find_element_by_xpath('//div[@class="cnt"]/p[2]/a').text
        create_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        # elementss = browser.find_elements_by_xpath('//*[@class="m-cmmt"]/div[2]/div/div[2]/div[1]/div')
        elementss = browser.find_elements_by_xpath('//*[@class="m-cmmt"]/div[2]/div/div[2]')

        for items in elementss:
            auto_avatar = items.find_element_by_xpath('../div[1]/a/img').get_attribute("src")
            likes = items.find_element_by_xpath('./div[@class="rp"]/a[1]').text

            index = items.find_element_by_xpath('./div[1]/div').text.index('：') + 1
            auto_name = items.find_element_by_xpath('./div[1]/div').text[:index-1]
            content = items.find_element_by_xpath('./div[1]/div').text[index:]  # 解析评论
            print(content,auto_name)
            comment_createtime = items.find_element_by_xpath('./div[@class="rp"]/div').text
            print(comment_createtime)
            le = len(content)
            if(le > 8):
                cursor.execute(sql, [content,music_name,singer,auto_name,img,comment_createtime,album,create_at,mid,auto_avatar,likes])

        conn.commit()


cursor.close()
conn.close()
browser.quit()