# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time


'''
“–no-sandbox”参数是让Chrome在root权限下跑
“–headless”参数是不用打开图形界面

可以额外加这些参数获得更好体验
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-gpu')
'''
chrome_options = Options()
#chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-gpu')

#UA
#chrome_options.add_argument('--user-agent=%s' % ua)



def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def get_ipcnt():
    return requests.get("http://127.0.0.1:5010/get_status/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

proxy = get_proxy().get("proxy")
print('--proxy-server=http://%s' % proxy)

ipcnt = get_ipcnt().get('count')
print('ipcnt = %d' % ipcnt)




#Proxy
chrome_options.add_argument('--proxy-server=http://%s' % proxy)

#启动
browser = webdriver.Chrome(chrome_options=chrome_options)
#browser.delete_all_cookies()

url1 = 'http://77m.live/portal.php?x=829270'
url0 = 'https://www.baidu.com/'

for i in range(1, ipcnt):
    print('%d' % i);
    browser.get(url0)
    print(browser.title)

    browser.get(url1)
    time.sleep(5)
    print(browser.title)
    #print(browser.page_source)

    delete_proxy(proxy)


ipcnt = get_ipcnt().get('count')
print('ipcnt = %d' % ipcnt)
browser.quit()

'''
browser.get(url0)
print(browser.title)

browser.get(url1)
time.sleep(5)
print(browser.title)
#print(browser.page_source)

delete_proxy(proxy)
ipcnt = get_ipcnt().get('count')
print('ipcnt = %d' % ipcnt)
browser.quit()
'''
