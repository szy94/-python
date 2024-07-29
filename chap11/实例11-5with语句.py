'''
with语句：又称上下文管理器，在处理文件时，无论是否产生异常，都能保证with语句执行完毕后关闭已经打开的文件，这个过程是自动的
语法结构：
with open（........）as file：
    pass
'''
def write_fun():
    with open('aa.txt','w',encoding='utf-8')as file:
        file.write('2020北京冬奥会')

def read_fun():
    with open('aa.txt','r',encoding='utf=-8')as file:
        file.read()
def copy(src_file,target_file):
    with open(src_file,'r',encoding='utf-8')as file:
        with open(target_file,'w',encoding='utf-8')as file2:
            file2.write(file.read())

if __name__ == '__main__':
    write_fun()
    read_fun()
    copy('./aa.txt','./dd.txt')