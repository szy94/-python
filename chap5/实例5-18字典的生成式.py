import random
#d={key:value for item in range(x)}
d={item:random.randint(1,100)for item in range(5)}#生成五个元素，key的值从0到5，不包括5
print(d)
'''
lst1=[]
lst2=[]
d={key:value for key,value in zip(lst1,lst2)}
'''
lst1=[1001,1002,1003]
lst2=['szy','dze','xwy']
d={key:value for key,value in zip(lst1,lst2)}
print(d)
#列表有序可变。元组有序不可变。字典无序可变，集合无序可变
#列表用[]，元组用（）,字典用{},集合用{}