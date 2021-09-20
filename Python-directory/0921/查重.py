# 当前时间:2021/9/21 3:28
from openpyxl import Workbook,load_workbook
wb=load_workbook('手机号.xlsx')
sh=wb['Sheet1']
index=[]
tmp=[]
for i,row in enumerate(sh.rows):
    for j,cell in enumerate(row):
        if cell.value not in tmp:
            tmp.append(cell.value)
        else:
            index.append((i,j))
print(tmp)
print(index)