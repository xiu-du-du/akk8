# 当前时间:2021/9/11 3:13
# 1. 定位到2021必看热片
# 2. 从2021必看热片中提取到子页面的链接地址
# 3. 请求子页面的链接地址，拿到我们想要的下载地址......

import requests
import re
domain='https://dytt89.com/'
resp=requests.get(domain,verify=False)   # verify=False去掉安全验证
resp.encoding='gb2312'  # 也可以写gbk，gbk和gb2312都是国标

# 拿到ul里的li
# 首页正则，找出列表ul
obj1=re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
# ul列表正则，找出ul列表里的子链接
obj2=re.compile(r"<a href='(?P<href>.*?)'")
# 子页面正则，找出电影下载链接和片名
obj3 = re.compile(r'◎片　　名　(?P<name>.*?)<br />.*?<td style="WORD-WRAP: br'
                  r'eak-word" bgcolor="#fdfddf"><a href="(?P<down>.*?)">', re.S)

# 匹配主页面2021必看热片里的ul列表，获取到ul的返回源代码
result1=obj1.finditer(resp.text)
# 设置一个空列表用来存放子页面链接
child_href_list=[]
# 遍历主页面里ul的数据
for it in result1:
    ul=it.group('ul')
    result2=obj2.finditer(ul)  # 匹配ul里子页面链接
    # 遍历ul里匹配到的子页面链接
    for itt in result2:
        href=itt.group('href')   # 拿到子页面链接的数据
        child_href=domain+href.strip('/')   # 拼接主域名
        child_href_list.append(child_href)  # 将完整的子页面链接存放到列表中
# 提取子页面内容
# 遍历列表中存放的子页面链接
for href in child_href_list:
    child_resp=requests.get(href,verify=False)   # 请求每个子页面链接
    child_resp.encoding='gb2312'   # 设置编码
    result3=obj3.finditer(child_resp.text)   # 匹配每个子页面中的下载地址和片名
    # 遍历匹配到的下载地址和片名
    for i in result3:
        down=i.group('down')   # 获取到下载地址
        name=i.group('name')   # 获取到片名
        print(name)
        print(down)
        print('===')

