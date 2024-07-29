'''
all(iter)判断iter中所有元素是否都为True
any(iter)判断iter中所有元素是否都为False
next（iter）获取迭代器下一个元素
filter（function，iter）通过指定条件过滤序列并返回一个迭代器对象
map（function，iter）通过函数function对可迭代对象iter的操作返回一个迭代器对象
'''
lst=[54,56,77,4,567,34]
#(1)排序操作
asc_lst=sorted(lst)#默认升序
dasc_lst=sorted(lst,reverse=True)
print(lst)
print(asc_lst)
print(dasc_lst)
#(2)reversed反向
new_lst=reversed(lst)
print(type(new_lst))#<class 'list_reverseiterator'>
print(new_lst)
print(list(new_lst))
#(3)zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
# print(type(zipobj))#<class 'zip'>
# print(list(zipobj))
#(4)enumerate
enum=enumerate(y,start=1)
print(type(enum))
print(list(enum))
print(tuple(enum))
#(5)all(iter)
lst2=[10,20,'',30]
print(all(lst))
print(all(lst2))
#(6)any(iter)
print(any(lst))
print(any(lst2))
#(7)next(iter)
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))
#(8)filter(function,iter)
def fun(num):
    return num%2==1
obj=filter(fun,range(10))
print(list(obj))#[1, 3, 5, 7, 9]
#(9)map(function,iter)
def upper(x):
    return x.upper()
new_lst2=['hello','world','python']
obj2=map(upper,new_lst2)#函数作为参数，不是调用所以不能写陈upper（）
print(list(obj2))
