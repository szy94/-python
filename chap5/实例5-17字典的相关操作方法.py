'''
d.keys()获取所有的key数据
d.values（）获取所有的value数据
d.pop（key，default）key存在获取相应的value，同时删除key-value对，否则获取默认值
d.popitem（）随机从字典中取出一对key-value，结果为元组类型，同时将这对key-value删除
d.clear清空字典中的所有key-value对
'''
lst1=[10,20,30,40,50]
lst2=['cat','dog','pet','zoo','uoin']
ziplst=zip(lst1,lst2)
d=dict(ziplst)
print(d)
print('-'*100)
keys=d.keys()
print(list(keys))
print(tuple(keys))
print(keys)
print('-'*100)
print(d.values())
print(d.pop(20))
print(d.pop(1001,'不存在'))
print(d.popitem())
print('-'*100)
values=d.values()
print(values)
print(list(values))
print(tuple(values))
print('-'*100)



print('^'*100)
lst=list(d.items())
print(lst)

print('^'*100)
d=dict(lst)
print(d)
print('^'*100)


#直接向字典中添加元素
d[60]='panda'
print(d)

d.clear()
print(d)

print(bool(d))#python中一切皆对象，每个对象都有一个bool值