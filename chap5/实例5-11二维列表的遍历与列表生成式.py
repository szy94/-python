lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',104,504],
    ['深圳',100,39]
]
print(lst)
for row in lst:
    for column in row:
        print(column,end='\t')
    print()#换行
#列表生成四行五列的二维列表
lst2=[[j for j in range(5)]for i in range(4)]
print(lst2)