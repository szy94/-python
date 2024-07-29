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

stu=Student('ysj',18)
stu2=Student('cmm',20)
print(stu.name,stu.age)
print(stu2.name,stu2.age)

#为stu2绑定一个实例属性
stu2.gender='男'
print(stu2.name,stu.age,stu2.gender)

#动态绑定方法
def introduce():
    print('我定义在类的外部，是一个普通的函数，我被动态绑定成了stu2对象的方法')
stu2.fun=introduce#本语句为函数的赋值，千万不能写成stu2.fun=introduce（），因为一旦加上（）就是调用
#此时，fun就是stu2对象的方法了
#调用
stu2.fun()