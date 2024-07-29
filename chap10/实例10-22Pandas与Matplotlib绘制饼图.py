import pandas as pd
import matplotlib.pyplot as plt
#读取Excel文件
df=pd.read_excel('手机销售数据.xlsx')
# print(df)
#解决中文乱码问题
plt.rcParams['font.sans-serif']=['chinese']
#设置画布的大小
plt.figure(figsize=(10,6))
labels=df['商品名']
y=df['北京出库销量']
print(labels)
print(y)
plt.pie(y,labels=labels,autopct='%1.1f%%')
#设置x，y轴刻度
plt.axis('equal')
plt.title('2020年北京各手机品牌出库量占比图')
#显示出来
plt.show()


