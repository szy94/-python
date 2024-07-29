class Student():
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender

    #使用装饰器@property属性 修饰方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender
    #将gender这个属性设置为可写属性
    @gender.setter
    def gender(self,value):
        if value!='男'and value!='女':
            print('性别有误，已将性别默认设置为男')
            self.__gender='男'
        else:
            self.__gender=value


stu=Student('szy','女')
print(stu.name,stu.gender)
#尝试修改属性的值
#stu.gender='男'#AttributeError: can't set attribute
stu.gender='其他'
print(stu.name,stu.gender)