# 当前时间： 2021-09-06 13:27
# 相对路径
# 绝对路径

import  os
print(os.getcwd())#获取当前工作目录
print(os.path.abspath('module1.py'))#当前文件的绝对路径
print(os.path.dirname(r'D:\Mrtai\!!!e语言学习进度\9月份\python\存放路径\0908\module1.py'))
print(os.path.dirname(r'\0907\module.py'))  #获取上一层文件夹的位置

#判断目录是否存在
print(os.path.exists('D:\Mrtai\!!!e语言学习进度\9月份\python\存放路径'))
print(os.path.exists(r'D:\Mrtai\!!!e语言学习进度\9月份\python\存放路径\aaa'))

#将目录和文件分开，返回文件名
print(os.path.split(r'D:\Mrtai\!!!e语言学习进度\9月份\python\存放路径\0908\module1.py'))

#返回文件的后缀名
print(os.path.splitext(r'D:\Mrtai\!!!e语言学习进度\9月份\python\存放路径\0908\module1.py'))

#判断是不是文件
print(os.path.isfile('module1.py'))
print(os.path.isfile(r'D:\Mrtai\!!!e语言学习进度\9月份\python\存放路径\0908'))

#判断是不是目录
print(os.path.isdir('module1.py'))
print(os.path.isdir(r'D:\Mrtai\!!!e语言学习进度\9月份\python\存放路径\0908'))

#返回目录内的文件-list
print(os.listdir(r'D:\Mrtai\!!!e语言学习进度\9月份\python\存放路径\0907'))
