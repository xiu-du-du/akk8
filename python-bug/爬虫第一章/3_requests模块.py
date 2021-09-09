# 当前时间： 2021-09-10 3:52
import requests
query = input('输入要搜索的关键词：')
url = f'https://www.sogou.com/web?query={query}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}    # 使用请求头伪装
resp = requests.get(url, headers=headers)  # 返回状态码200
print(resp)
print(resp.text)  # 取返回文本
resp.close()
