# lambda函数语法结构
# result=lambda 参数列表：表达式
def calc(a,b):
    return a+b
print(calc(10,20))

#匿名函数
s=lambda a,b:a+b#s表示匿名函数
print(type(s))
#调用匿名函数
print(s(10,20))

lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print()

for i in range(len(lst)):
    result=lambda x:x[i]#根据索引取值，result的类型是function
    print(result(lst))