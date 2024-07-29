class Person(object):#==class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'大家好，我叫{self.name},我今年：{self.age}岁')
per=Person('szy',18)#创建对象时，会自动调用————init————（）方法
print(dir(per))
print(per)#自动调用了————str————方法