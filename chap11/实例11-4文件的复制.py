def copy(src,new_path):
    #文件的复制就是边读边写操作
    #（1）打开源文件
    file1=open(src,'rb')
    #(2)打开目标文件
    file2=open(new_path,'wb')
    #(3)开始复制，边读边写
    s=file1.read()
    file2.write(s)
    #(4)关闭
    file2.close()#后打开的先关
    file1.close()#先打开的后关
if __name__ == '__main__':
    src='./google.jpg'# .代表的是当前目录
    new_path='../chap10/copy.jpg'#..代表从当前文件退出到上一级文件夹chap级，/chap10表示进入chap文件夹下，copy.jpg为图片的名称和类型
    copy(src,new_path)
    print('文件复制完毕')