'''
函数名称                描述说明
getcwd（)              获取当前的工作路径
listdir(path)          获取path路径下的文件和目录信息，如果没有指定path, 则获取当前路径下的文件和目录信息
mkdir(path)            在指定路径下创建目录（文件夹）
makedirs(path)         创建多级目录
rmdir(path)            删除path下的空目录
removedirs(path)       删除多级目录
chdir(path)            把path设置为当前目录
walk(path)              遍历目录树，结果为元组，包含所有路径名、所有目录列表和文件列表
remove(path)            删除path指定的文件
rename(old, new)        将old重命名为new
stat(path)              获取path指定的文件信息
startfile(path)          启动path指定的文件
'''
import os

#删除文件
# os.remove('./a.txt')
#重命名
# os.rename('./aa.txt','./aaa.txt')
# s=os.stat('./aaa.txt')
# print(s)
#启动python解释器
os.startfile('C:\Program Files\Python38\python.exe')