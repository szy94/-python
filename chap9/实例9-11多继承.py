class FatherA():
    def __init__(self,name):
        self.name=name
    def showA(self):
        print('父类A中的方法')
class FatherB():
    def __init__(self,age):
        self.age=age
    def showB(self):
        print('父类B中的方法')
class Son(FatherA,FatherB):
    def __init__(self,name,age,gender):
        #调用父类的初始化方法，此时不能再用super（）.———init——（）方法去调用父类的初始化方法，因为此时有两个父类
        #需要调用两个父类的初始化方法
        FatherA.__init__(self,name)
        FatherB.__init__(self,age)
        self.gender=gender

son=Son('szy',20,'女')
son.showA()
son.showB()