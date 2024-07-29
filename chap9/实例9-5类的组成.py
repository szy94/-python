class Student:
    # 类属性：定义在类当中，方法外的变量
    school = '北京XXX教育'

    # 实例属性：定义在————init————方法中，使用self打点的变量,实例属性可以在整个类当中去使用
    def __init__(self, xm, age):  # xm,age是方法的参数，是局部变量，xm和age的作用域是整个————init————方法
        self.name = xm  # =左侧是实例属性，xm是局部变量，将局部变量的值xm赋值给实例属性self.name
        self.age = age  # 实例的名称和局部变量的名称可以相同

    #定义在类中的函数，称为方法，自带一个参数self
    def show(self):#实例方法的定义
        print(f'我叫：{self.name},今年：{self.age}岁了')#实例属性可以在整个类当中去使用

#静态方法
# 使用@staticmethod修饰的方法是静态方法

    @staticmethod
    def sm():
   # self.name 报错
   # self.show()报错
        print('这是一个静态方法，在静态方法中不能调用实例属性，也不能调用实例方法')

#类方法
# 使用@classmethod修饰的方法是类方法
    @classmethod
    def cm(cls):
    # self.name
    # self.show()
        print('这是一个类方法，在类方法中，不能调用实例属性和实例方法')

#创建类的对象
stu=Student('szy',18)#为什么传入两个参数？因为————init————方法中有两个形参，self是自带的参数，无需手动传入
#实例属性，是使用对象名进行打点调用的
print(stu.name,stu.age)#实例属性可以在整个类当中去使用
#类属性，直接使用类名去打点调用
print(Student.school)

#实例方法，使用对象名进行打点调用（只要和实例有关的都是用对象名进行打点调用）
stu.show()
#类方法，直接使用类名打点调用
Student.cm()
#静态方法，直接使用类名打点进行调用
Student.sm()











