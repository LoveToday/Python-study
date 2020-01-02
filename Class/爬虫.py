"""请求网页"""
import requests
import re
import time
import os

# /// <head><title>403 Forbidden</title></head> 这个是反爬虫
# User-Agent 告诉服务器身份

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0', 
     'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'
}

response = requests.get('http://sc.chinaz.com/tupian/190907013750.htm', headers=headers)
# print(response.request.headers)
# {'User-Agent': 'python-requests/2.22.0', 
# 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
print(response.text)

html = response.text

dir_name = re.findall('', html)[-1]
if not os.path.exists(file_name):
    os.mkdir(dir_name)


# 解析网页
# http://pics.sc.chinaz.com/files/pic/pic9/201908/zzpic19465.jpg

urls = re.findall('<a href="(.*?)"\
 title=".*?" \
class="image_gall"><img src="(.*?)" \
alt=".*?" border="0"><p></p></a>', html)

# urls = re.findall('<a href="(.*?)" alt=".*?">')
print('=----------')
print(urls)



for url in urls:
    time.sleep(1)
    # 图片的名字
    file_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    with open(file_name, 'wb') as f:
        f.write(response.content)
