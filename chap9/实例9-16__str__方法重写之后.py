class Person(object):#==class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #方法重写
    def __str__(self):
        return '这是一个人类，具有name和age两个实例属性'#返回值是个字符串
per=Person('SZY',18)
print(per)
print(per.__str__())