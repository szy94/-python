d={'hellow':10,'world':20,'python':30}
#第一种访问字典中的方式
print(d['hellow'])
#第二种访问字典的方式
print(d.get('hellow'))
#二者之间的区别是，如果key不存在，d[key]这种情况它会报错d.get（key）可以指定默认值


#print([d['java']])
print(d.get('java'))
print(d.get('java'),'不存在')
#字典的遍历
for item in d.items():#必须是d.items()，不能是d.i()
    print(item)
for i in d.items():
    print(i)
#使用for循环遍历时，分别获取key，value
for key,value in d.items():
    print(key,value)
for i,j in d.items():
    print(i,j)