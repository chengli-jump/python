import pandas as pd  
#将所安装包引入到当前搜索列表中
import sys
sys.path.append('data/home/aistudio/external-libraries')

jiangsu = pd.read_excel("data/home/aistudio/data/data20465/jiangsu.xls")
#写出xlsx
jiangsu.to_excel('data/home/aistudio/work/files/jiangsu.xlsx')

cpi = pd.read_excel("data/home/aistudio/data/data20465/cpi.xls")
cpi.columns = cpi.iloc[1]    # ⑤
cpi = cpi[2:]    # ⑥
cpi.drop([11, 12], axis=0, inplace=True)    # ⑦
cpi['cpi_index'] = ['总体消费', '食品烟酒', '衣着', '居住', '生活服务', '交通通信', '教育娱乐', '医保', '其他']    # ⑧
cpi.drop(['指标'], axis=1, inplace=True)    # ⑨
cpi.reset_index(drop=True, inplace=True)    # ⑩
cpi.columns.rename('', inplace=True)    # ⑪

print(cpi)
#可以看出每列的数据不是浮点或整型
print(cpi.dtypes)
#转换为浮点型
for column in cpi.columns[:-1]:
    cpi[column] = pd.to_numeric(cpi[column])
print(cpi.dtypes)

import matplotlib.pyplot as plt

plt.bar(cpi.iloc[5,:-1].index,cpi.iloc[5,:-1].values)
print(jiangsu)
plt.show()

plt.bar(jiangsu['name'],jiangsu['area'])
plt.show()
