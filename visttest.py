# -*- coding: utf-8 -*-
print('mymain检查点1')
import requests
import time
print('mymain检查点2')
def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code
print('mymain检查点3')
def getHtml():
    # ....
    url = 'http://77m.live/portal.php?x=829270'
    headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    
    retry_count = 1
    proxy = get_proxy().get("proxy")
    print('mymain检查点4')
    while retry_count > 0:
        print('mymain检查点5')
        try:
            print('mymain检查点6')
            html = requests.get(url, allow_redirects=True, headers=headers, proxies={"http": "http://{}".format(proxy)})
            print(html.text)
            print('---------------------------------------------------')
            time.sleep(3)
            html = requests.get(url, headers=headers, proxies={"http": "http://{}".format(proxy)})
            print(html.text)
            # 使用代理访问
            return html
        except Exception:
            print('mymain检查点7')
            print("eeeeeee")
            retry_count -= 1
    # 删除代理池中代理
    delete_proxy(proxy)
    print("delete_proxy")
    return None
    
getHtml()