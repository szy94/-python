#{}直接创建集合
s={10,20,30,40,'szy'}
print(s)#集合中只能存储不可变数据类型
#使用set（）创建集合

s=set()#创建了一个空集合
print(type(s))
print(s)
s={}#直接使用{}创建空的东西，是字典不是集合，s=set()创建了一个空集合
print(type(s))

s=set('helloworld')
print(s)#集合是无序的,并不会输出helloworld
s1=set([10,20,30])
print(s1)
s2=set(range(1,10))
print(s2)
print(max(s2))
print(min(s2))
print(len(s2))
print(9 in s2)
#集合的删除操作
del s2
print(s2)

