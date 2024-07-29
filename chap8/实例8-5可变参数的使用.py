def fun(*para):#*para个数可变的位置传参，将参数放入元组中
    print(type(para))
    for item in para:
        print(item)

fun(10,20,30,40)
fun(10)
fun([11,22,33,44])#实际上传递的是一个参数
#在调用时，参数前加一颗星，会将列表解包
fun(*[11,22,33,44])

#个数可变的关键字参数加**，将参数放入字典中
def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,value)
fun2(name='szy',age=18,height=173)
d={'name':'szy','age':18,'height':175}
#fun2(d)
fun2(**d)#系列解包操作