# 当前时间:2021/9/11 2:01
# 拿到页面源代码。  request模块
# 通过正则来提取有效信息。  re模块
import requests
import re
import csv

num1=0
while num1 <= 250:
    url ="https://movie.douban.com/top250?start="+str(num1)+"&filter="
    headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        }
    resp=requests.get(url,headers=headers)
    page_content=resp.text

    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>.*?(?P<year>\d+)&nbsp.*?<span'
                     r' class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                     r'<span>(?P<num>.*?)</span>',re.S)
    ret=obj.finditer(page_content)
    f=open('data.csv',mode='a',encoding='utf-8')
    csv_writer=csv.writer(f)
    for i in ret:
        # print(i.group('name'),end='    ')
        # print(i.group('year'),end='    ')
        # print(i.group('score'),end='    ')
        # print(i.group('num'))
        dic=i.groupdict()
        csv_writer.writerow(dic.values())
    num1+=25
f.close()
print('ok')