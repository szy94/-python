#写入
def my_write():
    #(1)（创建）打开文件
    #语法格式为：变量名=open('路径名（文件名）'，'mode',encoding)mode表示是读还是写，w是写，r是读，encoding是编码格式
    file=open('a.txt','w',encoding='utf-8')#如果在路径名下直接写文件名，那么该文件会存储在当前python文件的路径下
    #(2)操作文件
    #语法格式为：变量名.read（）  变量名.write（s）
    file.write('伟大的中国梦')
    #关闭文件
    #语法格式为：变量名.close（）
    file.close()

#读取
def my_read():
    # (1)（创建）打开文件
    # 语法格式为：变量名=open('路径名（文件名）'，'mode',encoding)mode表示是读还是写，w是写，r是读，encoding是编码格式
    file1 = open('a.txt', 'r', encoding='utf-8')  # 如果在路径名下直接写文件名，那么该文件会存储在当前python文件的路径下
    # (2)操作文件
    # 语法格式为：变量名.read（）  变量名.write（s）
    s=file1.read()
    print(s)
    # 关闭文件
    # 语法格式为：变量名.close（）
    file1.close()
#主程序运行
if __name__ == '__main__':
    my_write()#调用函数
    my_read()