#列表的第一种创建方式
lst=['hello','world','98',95]
print(lst[0],lst[1])
print(lst)
#列表的第二种创建方式
lst1=list('helloworld')
print(lst1[0],lst1[1])
print(lst1)
lst2=list(range(1,10,2))
print(lst2)
print(lst1+lst2+lst)
print(lst1*3)
print('h' in lst1)
print('h' not in lst1)
print(len(lst1))
print(max(lst1))
print(min(lst1))
print(lst1.index('e'))
print(lst1.count('l'))
#列表的删除
lst3=list('5898455211')
print(lst3)
del lst3
print(lst3)