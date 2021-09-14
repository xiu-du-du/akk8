# 当前时间:2021/9/14 19:24
s='hello python'
print(s.center(20,'*'))   # 左右填充4个
print(s.ljust(20,'*'))   # 右填充8个
print(s.rjust(20,'*'))   # 左填充8个
print(s.zfill(10))   # 使用0进行左填充
print('-100'.zfill(10))   # 使用0进行左填充