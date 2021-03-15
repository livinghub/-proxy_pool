# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
import sys


'''
“–no-sandbox”参数是让Chrome在root权限下跑
“–headless”参数是不用打开图形界面

可以额外加这些参数获得更好体验
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-gpu')
'''
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
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


url1 = 'http://77m.live/portal.php?x=829270'
url0 = 'https://www.baidu.com/'

#查看ip池数目
def ipcnt():
    ipcnt = get_ipcnt().get('count')
    print('ipcnt = %d' % ipcnt)


def vist():
    ipcnt = get_ipcnt().get('count')
    while ipcnt > 0:
        
        print('ipcnt = %d' % ipcnt)
        #设置Proxy
        proxy = get_proxy().get("proxy")
        print('--proxy-server=http://%s' % proxy)
        chrome_options.add_argument('--proxy-server=http://%s' % proxy)
        delete_proxy(proxy)
        
        try:
            #启动
            browser = webdriver.Chrome(chrome_options=chrome_options)
            #browser.delete_all_cookies()
            browser.set_page_load_timeout(10)
            
            #browser.get(url0)
            #print(browser.title)
            browser.get(url1)
            time.sleep(3)
            print(browser.title)
            #print(browser.page_source)
        except TimeoutException:
                print '！！！！！！time out after 10 seconds when loading page！！！！！！'
                # 当页面加载时间超过设定时间，通过js来stop，即可执行后续动作
                pass
        except WebDriverException:
            print('!!!!!!!!!!!!!!!!!!!WebDriverException错误，删除了一个ip!!!!!!!!!!!!!!!!!!!!!!!!!')
            pass
        finally:
            ipcnt = get_ipcnt().get('count')
            browser.quit()


def main(argv):

    if str(sys.argv[1]) == 'ipcnt':
        ipcnt()
    elif str(sys.argv[1]) == 'vist':
        vist()


if __name__ == "__main__":
   main(sys.argv)
