# 当前时间:2021/9/12 5:43
# 1. 拿到主页面源代码，提取子页面的链接地址(href)
# 2. 通过href拿到子页面的内容，从子页面中找到图片的下载地址 img->src
# 3. 下载图片

import requests
from bs4 import BeautifulSoup

url='https://umei.cc/bizhitupian/meinvbizhi/yangyanmeinv.htm'
headers= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                  '/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
print(resp.text)


