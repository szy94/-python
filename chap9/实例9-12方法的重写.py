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
    def show(self):#将父类Person的方法进行重写
        #调用父类中的方法
        super().show()
        print(f'我来自XXX大学，我的学号是：{self.sno}')
#Docter继承person类
class Docter(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department
    def show(self):#完全重写方法体
        #super().show()#调用父类中的方法
        print(f'大家好我叫：{self.name},我今年{self.age}岁，我工作的科室是：{self.department}')#完全重写方法体
#创建第一个子类对象
stu=Student('SZY',20,'20205101104')
stu.show()#由于子类有show方法因此这里调用的是子类的show方法
docter=Docter('dzm',32,'外科')
docter.show()#同理这里调用的也是子类自己的show方法
