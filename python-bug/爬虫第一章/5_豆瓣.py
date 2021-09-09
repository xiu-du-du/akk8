# 当前时间： 2021-09-10 4:30
import requests
url='https://movie.douban.com/j/chart/top_list'
# 重新封装参数
param={
    'type': '24',
    'interval_id': '100:90',
    'action':'',
    'start': 0,
    'limit': 20,
}
# 获取不到内容，就使用请求头进行伪装后再爬取
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
resp=requests.get(url,params=param,headers=headers)
print(resp)
print(resp.url)
print(resp.json())