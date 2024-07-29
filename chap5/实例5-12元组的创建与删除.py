#元组的第一种创建方式,元组是不可变数据类型
t=('szy','dzm','wxy','s',[10,20,30])
print(t)
#元组的第二种创建方式,使用tuple()
t=tuple('helloworld')
print(t)
t=tuple([10,20,30,40])
print(t)
print(10 in t)
print(max(t))
print(min(t))
print(len(t))
print(t.index(20))
print(t.count(20))

print('_'*100)
x=tuple([10])
print(type(x))
y=tuple([10],)
print(type(y))
m=(10)
print(type(m))
n=(10,)#如果元组中只有一个元素，逗号不能省去
print(type(n))
#元组的删除del
del t
#print(t)