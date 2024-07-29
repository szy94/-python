class Person():
    #有实例属性才写init（）初始化方法
    def eat(self):
        print('人，吃五谷杂粮')
class Cat():
    def eat(self):
        print('猫，喜欢吃鱼')
class Dog():
    def eat(self):
        print('狗，喜欢啃骨头')
#这三个类中都有一个同名的方法，eat
#编写函数
def fun(obj):#obj是形式参数，但是在定义时并不知道这个形参的数据类型
    obj.eat()#通过变量obj调用eat方法
#创建三个类的对象
per=Person()#由于没有定义初始化方法，所以不用传参
cat=Cat()
dog=Dog()
#调用fun函数
fun(per)
fun(cat)
fun(dog)