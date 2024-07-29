#第一种遍历方法，使用for循环进行遍历列表
lst=list('hello')
for index in lst:
    print(index)
#第二种
for i in range(0,len(lst)):
    print(lst[i])
#第三种enumerate函数
for index,item in enumerate(lst):
    print(index,item)#index是序号不是索引
for index,item in enumerate(lst,start=1):
    print(index,item)
