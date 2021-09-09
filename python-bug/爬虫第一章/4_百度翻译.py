# 当前时间： 2021-09-10 4:11
import requests
url = 'https://fanyi.baidu.com/sug'
s=input('请输入要翻译的英文单词：')
data = {
    'kw': s
}
# 发送post请求，发送的数据必须放在字典中，通过data参数进行发送
resp = requests.post(url, data=data)
print(resp)
print(resp.json()) # 将服务器返回的内容直接处理成json()  => dict字典
resp.close()
