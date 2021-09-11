# 当前时间:2021/9/12 4:13
# 安装清华源
# pip install bs4

# 1. 拿到页面源代码
# 2. 使用bs4 进行解析
import csv
import requests
from bs4 import BeautifulSoup
url = 'http://xinfadi.com.cn/getPriceData.html'
resp=requests.get(url)   # 获取页面源代码
text=resp.json()   # 获取菜品json
f=open('caijia.csv',mode='w',encoding='utf-8')
csv_writer=csv.writer(f)
for i in text['list']:   # 遍历json键值‘list’内的数据
    prodName=i['prodName']  # 打印输出key:‘proName’的值
    lowPrice=i['lowPrice']
    avgPrice=i['avgPrice']
    highPrice=i['highPrice']
    pubDate=i['pubDate']
    csv_writer.writerow([prodName,lowPrice,avgPrice,highPrice,pubDate])   # 写到csv文件
print(type(text))
f.close()
# =====================================================================
# 网站已改版，下面方法过期。
# =====================================================================
# 1. 把页面源代码交给BeautifulSoup()进行处理，生产bs对象
# page=BeautifulSoup(resp.text,'html.parser')   # 指定html
# 2. 从bs对象中查找数据
# find(标签，属性=值) 和 find_all(标签，属性=值)    find只找第一个，find_all全部找出来
# table=page.find("table",class_="hq_table")   #class是python中的关键字，加_为了区分
# table=page.find("table",attrs={"class":"hq_table"})    # 和上一行是一个意思，避免class
# 拿到所有数据行
# trs =table.find_all("tr")[1:]   #不拿表格的标题，所以设置从1开始往后拿
# for tr in trs:
#     tds=tr.find_all("td")   # 拿到每行中的所有td
#     name=tds[0].text   # .text 表示拿到被标签标记的内容
#     low=tds[1].text   # .text 表示拿到被标签标记的内容
#     avg=tds[2].text   # .text 表示拿到被标签标记的内容
#     high=tds[3].text   # .text 表示拿到被标签标记的内容
#     gui=tds[4].text   # .text 表示拿到被标签标记的内容
#     kind=tds[5].text   # .text 表示拿到被标签标记的内容
#     date=tds[5].text   # .text 表示拿到被标签标记的内容
#     csv_writer.writerow([name,low,avg,high,gui,kind,date])
# f.close()
# print("ok")