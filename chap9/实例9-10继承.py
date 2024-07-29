'''
继承的语法
class 类名（父类1，父类2，.......）：#四个空格一个缩进
    pass
'''
class Person:#默认继承object
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
#Student继承Person类
class Student(Person):#Student继承Person后就拥有了Person类中的公有和受保护的东西
    def __init__(self,name,age,sno):
        super().__init__(name,age)#调用父类的初始化方法，目的是为name和age赋值
        self.sno=sno
#Docter继承person类
class Docter(Person):    
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department
#创建第一个子类对象
stu=Student('SZY',20,'20205101104')
stu.show()#由于子类没有自己的show方法，因此这里调用的是父类的show方法
docter=Docter('dzm',32,'外科')
docter.show()#由于子类没有自己的show方法，因此这里调用的是父类的show方法
