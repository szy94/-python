class CPU():
    pass
class Disk():
    pass
class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
cpu=CPU()
disk=Disk()
com=Computer(cpu,disk)
com1=com
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com1,'子对象的内存地址：',com1.cpu,com1.disk)
print('*'*100)
#类对象的浅拷贝
import copy
com2=copy.copy(com)#com2是新产生的对象，com2的子对象cpu,disk不变
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com2,'子对象的内存地址：',com2.cpu,com2.disk)
#类对象的深拷贝
print('*'*100)
com3=copy.deepcopy(com)#com3是新产生的对象，com3的子对象cpu，disk也会重新产生
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com3,'子对象的内存地址：',com3.cpu,com3.disk)