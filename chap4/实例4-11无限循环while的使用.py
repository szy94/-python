answer=input('今天要上课吗？y/n：')#（1）初始化变量
while answer=='y':#（2）条件判断
    print('好好学习')#（3）语句块
    answer=input('今天要上课吗？y/n:')#（4）改变变量

#1-100之间的累加和
s=0
i=1
while i<=100:
    s+=i
    i+=1
print(s)