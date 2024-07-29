from datetime import datetime
from datetime import timedelta
#创建两个datetime类型的对象
delta1=datetime(2028,10,1)-datetime(2028,5,1)
print(delta1)
print(type(delta1))
a=datetime(2028,5,1)+delta1
print(type(a))
print(a)
#通过传入参数的方式创建一个timedelta对象
dt1=timedelta(10)
print('创建一个10天的timedelta对象:',dt1)
dt2=timedelta(10,11)
print('创建一个10天11秒的timedelta对象:',dt2)



