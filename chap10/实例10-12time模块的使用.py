import time
now=time.time()
print(now)
obj=time.localtime(1721813356.1041589)#struct_time
print('星期：',obj.tm_wday)#tm_wday从0开始算的。2表示星期三，3表示星期四，以此类推
print(obj)
obj2=time.localtime(60)#60秒
print(obj2)#1970年，1月，1日，8时，1分，0秒
print(type(obj2))
print('年份：',obj2.tm_year)
print('星期：',obj2.tm_wday)
print(time.ctime())
print(time.strftime('%Y-%m-%d',time.localtime()))#str指的是字符串，f指的是format格式化的意思
print(time.strftime('%H:%M:%S',time.localtime()))
print('月份的名称：',time.strftime('%B',time.localtime()))
print('星期的名称：',time.strftime('%A',time.localtime()))

print(time.strptime('2008-08-08','%Y-%m-%d'))
time.sleep(5)#休眠5秒后执行下面的语句
print('szy')

