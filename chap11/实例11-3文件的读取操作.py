'''
文件的打开模式                 模式说明
r (read)                   以只读模式打开，文件指针在文件的开头，如果文件不存在，程序抛异常
rb                   以只读模式打开二进制文件，如图片文件
w  (write)                  覆盖写模式，文件不存在则创建，文件存在则内容覆盖
wb                   覆盖写模式写入二进制数据，文件不存在则创建,文件存在则覆盖
a (add)                  追加写模式，文件不存在创建，文件存在，则在文件最后追加内容
+                    与w/r/a等一同使用，在原功能的基础上增加同时读写功能
'''
'''
读写方法                     描述说明
file.read(size)             从文件中读取size个字符或字节，如果没有给定参数，则读取文件中的全部内容
file.readline(size)         读取文件中的一行数据，如果给定参数，则为读取这一行中的size个字符或字节
file.readlines()            从文件中读取所有内容，结果为列表类型
file.write(s)               将字符串s写入文件
file.writelines(lst)        将内容全部为字符串的列表Ist写入文件
file.seek(offset)           改变当前文件操作指针的位置，英文占一个字节，中文gbk编码占两个字节，utf-8编码占三个字节
'''
def my_read(filename):
    #(1)打开文件
    file=open(filename,'w+',encoding='utf-8')
    #(2)操作文件
    file.write('你好啊')#写入完成，文件的指针在最后
    #seek修改文件指针的位置
    file.seek(0)
    #读取
    #s=file.read()读取全部
   # s=file.read(2)#读取两个中文字符
   # s=file.readline()#读取一行数据
   # s = file.readline(2)#读取一行中的两个中文字符
    #s=file.readlines()#读取所有，一行,为列表中的一个元素,两行就是在列表中有两个元素
    #若想只读取好啊，则可以利用file.seek（）移动指针的位置到3
    file.seek(3)#3表示的是三个字节，在utf-8当中一个中文占据3个字节，若采用gkb则进行相应的换算即可，若d.txt中全部都是英文字符，则光标位置就是file.seek（i）中i的位置
    s=file.read()#从1开始读取全部   你/好啊 /代表此时光标的位置
    print(type(s),s)
    #关闭文件
    file.close()
if __name__ == '__main__':
    my_read('d.txt')