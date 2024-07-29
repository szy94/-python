class Person(object):#==class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
per=Person('SZY',18)
print(per)
print(per.__str__())