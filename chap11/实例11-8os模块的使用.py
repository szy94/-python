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
print('获取当前的工作路径：',os.getcwd())
lst=os.listdir()
print('获取path路径下的文件和目录信息，如果没有指定path, 则获取当前路径下的文件和目录信息：',lst)
print('指定路径下所有的文件和目录信息：',os.listdir('E:/programsANDdocuments'))
#创建目录
#os.mkdir('好好学习')#如果要创建的文件夹存在，则报错：FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: '好好学习'
#os.makedirs('./aa/bb/cc')
#删除目录
#os.rmdir('./好好学习')#删除path下的空目录  ./表示当前目录  FileNotFoundError: [WinError 2] 系统找不到指定的文件。: './好好学习'
#os.removedirs('./aa/bb/cc')#  删除多级目录
#改变当前的工作路径
os.chdir('E:/programsANDdocuments/bilibilil learn Pyqt')
print('获取当前的工作路径：',os.getcwd())
os.chdir('E:/programsANDdocuments/bilibili learn python/chap11')
print('获取当前的工作路径：',os.getcwd())
#遍历目录树
# for dirs,dirlst,filelst in os.walk('E:/programsANDdocuments/bilibili learn python'):
#     print(dirs,dirlst,filelst)