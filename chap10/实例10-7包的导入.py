import admin.my_admin as a#包名.模块名
a.info()#init模块中的代码也会被执行

from admin import my_admin as b  #from 包名 import 模块名 as 别名
b.info()#init模块中的代码不会被执行了，因为在第一行和第二行代码中init已经执行过一次了

from admin.my_admin import info #from admin.my_admin import info
info()
from admin.my_admin import *  #from admin.my_admin import *
print(name)