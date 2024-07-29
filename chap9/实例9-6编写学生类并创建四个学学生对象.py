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
stu=Student('szy',18)
stu2=Student('dzm',20)
stu3=Student('wxy',22)
stu4=Student('fyx',23)
Student.school='帮帮教育'#给类的类属性赋值
#将学术对象存储到列表中
lst=[stu,stu2,stu3,stu4]#列表中的元素为student类型的对象
for item in lst:#item是列表中的元素，为student类型的对象
    item.show()#对象名打点调用实例方法

