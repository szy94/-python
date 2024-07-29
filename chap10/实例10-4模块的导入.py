from my_info import *
from introduce import *
#导入模块当中具有同名的函数和变量,后导入的会将之前导入的进行覆盖
info()
#如果不想覆盖，解决方法可以使用import
import my_info
import introduce
#此时使用模块中的函数或者变量时，可以使用模块名进行打点调用
my_info.info()
introduce.info()
