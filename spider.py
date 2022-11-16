from selenium import webdriver
import time
import pymysql


#获得音乐的id
def getId():
    try:
        arr=[]
        browser = webdriver.Chrome('/usr/local/bin/chromedriver')
        browser.get("https://music.163.com/#/discover/toplist?id=3779629")
        iframe_elemnt = browser.find_element_by_id("g_iframe")
        # iframe_elemnt = browser.find_element_by_id("g_iframe")
        browser.switch_to.frame(iframe_elemnt)
        elements = browser.find_elements_by_xpath('//tr')
        for item in elements:
            id = item.get_attribute('id')
            arr.append(id[:10])
            print(id)
        return arr
    except:
        print('获得id失败')
        return ''




def main():
    list = getId() 
    print(list)

main()