'''
s.add(x)如果x不在集合当中，则将x添加到s，否则等同于没有进行操作，集合中的元素不能重复,如果重复自动合并
s.remove(x)如果x在集合中则删除x，否则报错
s.clear()清空集合
'''
s={10,10,20,30,50,68,12}
print(s)
s.add(120)
print(s)
s.add(30)
print(s)
s.remove(10)
print(s)
#s.remove(130)
print(s)
print('_'*100)
#s.clear()
#print(s)
#集合的遍历操作
for i in s:
    print(i)
#使用enumerate进行遍历
print('*'*100)
for index,item in enumerate(s):
    print(index,item)
#集合的生成式
print('$'*100)
s={i for i in range(1,10)}
print(s)
s={i for i in range(1,10) if i%2==1}
print(s)