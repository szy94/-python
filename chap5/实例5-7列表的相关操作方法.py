lst=list('helloworld')
print(id(lst))
'''
lst.append(x) 在列表lst最后增加一个元素
lst.insert(index,x)在列表中第index位置增加一个元素
lst.clear（）清除列表lst中的所有元素
lst.pop(index)将列表lst中的第index位置的元素取出并删除
lst.remove(x)将列表lst中出现的第一个元素x删除
lst.reverse()将列表lst中的元素反转
lst.copy(lst)
'''
#列表是可变数据类型
lst.append('szy')
print(lst)
lst.insert(1,'dzm')
print(lst)
lst.pop(1)
print(lst)
lst.remove('h')
print(lst)
lst.reverse()
print(lst)
lst1=lst.copy()
print(lst1)