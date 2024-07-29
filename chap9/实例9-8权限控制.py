class Student():
    #首位双下划线，表示特殊的函数
    def __init__(self,name,age,gender):
        self._name=name #以单下划线开头表示：self._name是受保护protected，只能本类和子类访问
        self.__age=age#双下划线开头，self.__age表示私有的，只能类本身去使用
        self.gender=gender#普通的实例属性,类的内部，外部，及子类都可以去访问

    def _fun1(self):#受保护的
        print('子类及本身可以访问')

    def __fun2(self):#私有的
        print('只有定义的类可以访问')
    def show(self):
        self._fun1()#类本身访问受保护的方法
        self.__fun2()#类本身访问私有方法
        print(self._name)#受保护的实例属性
        print(self.__age)#私有的实例属性
#创建一个学生类的对象
stu=Student('szy',20,'女')
#现在的位置处于类的外部
print(stu._name)
# print(stu.__age)
#访问受保护的实例方法
stu._fun1()
#访问私有的实例方法
#stu.__fun2()

#私有的实例属性和方法真的完全不能访问吗？   并不是，按照下列方法可以访问
print(stu._Student__age)
stu._Student__fun2()
print(dir(stu))