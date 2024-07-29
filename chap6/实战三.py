lst=[
    ['01','风扇','美的',500],
    ['02','洗衣机','TCL',1000],
    ['03','微波炉','老板',500],
]
print('编号\t\t名称\t\t品牌\t\t价格')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()
for item in lst:
    item[0]='0000'+item[0]
    item[3]='${0:.2f}'.format(item[3])

for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()

