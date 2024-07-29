'''
第一种创建进程的语法结构：Process(group=None, target, name, args, kwargs)
参数说明：
1) group：表示分组，实际上不使用，值默认为None即可
2) target:表示子进程要执行的任务，支持函数名
3) name：表示子进程的名称
4) args:表示调用函数的位置参数，以元组的形式进行传递
5) kwargs:表示调用函数的关键字参数，以字典的形式进行传递

'''
from multiprocessing import Process
import os,time
#函数中的代码是进程要执行的代码
def test():
    print(f'我是子进程，我的PID是：{os.getpid()},我的父进程是:{os.getppid()}')
    time.sleep(1)

if __name__ == '__main__':
    print('主进程开始执行')
    lst=[]
    #创建五个子进程
    for i in range(5):
        p=Process(target=test)
        #启动子进程
        p.start()
        #启动中的进程添加到列表中
        lst.append(p)
        #遍历lst，列表中五个子进程
    for item in lst:      #item的数据类型是process
        item.join()#阻塞主进程
    print('主进程执行完毕')