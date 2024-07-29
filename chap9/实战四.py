class Car(object):
    def __init__(self,type,no):
        self.type=type
        self.no=no

    def start(self):
        print('启动！')

    def stop(self):
        print('停止')
class Taxi(Car):
    def __init__(self,type,no,company):
        super().__init__(type,no)
        self.company=company
    def start(self):
        print('乘客你好')
        print(f'我是{self.company}出租车公司，我的车牌是：{self.no},你要去哪里？')
    def stop(self):
        print('目的地到了，请付款后下车')
class FamilyCar(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name=name
    def start(self):
        print(f'我是{self.name},我的车我做主')
    def stop(self):
        print('目的地到了，我们下车')
taxi=Taxi('奔驰','豫EBQ262','滴滴')
taxi.start()
taxi.stop()
print('*'*100)
famliy_car=FamilyCar('xiaomi速7','京A88888','武大郎')
famliy_car.start()
famliy_car.stop()