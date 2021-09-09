# 当前时间： 2021-09-10 2:34
from  urllib.request import urlopen
resp=urlopen('http://www.baidu.com')

with open('mybaidu.html',mode='w',encoding="UTF-8") as f:
    f.write(resp.read().decode("UTF-8"))
print('over')