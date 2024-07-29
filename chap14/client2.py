#encoding='utf-8'
import threading

import wx
from socket import socket,AF_INET,SOCK_STREAM
class YsjClient(wx.Frame):
    def __init__(self,client_name):
        #调用父类的初始化方法去初始化窗体
        #pos窗体的打开位置
        #size:窗体的大小，单位是像素，400：宽  450：高
        wx.Frame.__init__(self,None,id=1001,title=client_name+'的客户端',pos=wx.DefaultPosition,size=(400,450))
        #创建面板对象
        pl=wx.Panel(self)
        #在面板中放上盒子
        box=wx.BoxSizer(wx.VERTICAL)#垂直方向布局
        #可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL)#水平方向布局
        #创建两个按钮
        conn_btn=wx.Button(pl,size=(200,40),label='连接')
        dis_conn_btn = wx.Button(pl, size=(200, 40), label='断开')
        #把两个按钮放到可伸缩的网格布局
        fgz1.Add(conn_btn,1,wx.TOP|wx.LEFT)
        fgz1.Add(dis_conn_btn,1,wx.TOP|wx.RIGHT)
        #将可伸缩的网格布局添加到box中
        box.Add(fgz1,1,wx.ALIGN_CENTRE)
        #只读文本框，显示聊天内容
        self.show_text=wx.TextCtrl(pl,size=(400,210),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.show_text,1,wx.ALIGN_CENTRE)
        #创建聊天内容的文本框
        self.chat_text = wx.TextCtrl(pl, size=(400, 120), style=wx.TE_MULTILINE )
        box.Add(self.chat_text, 1, wx.ALIGN_CENTRE)
        # 可伸缩的网格布局
        fgz2 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向布局
        # 创建两个按钮
        reset_btn = wx.Button(pl, size=(200, 40), label='重置')
        send_conn_btn = wx.Button(pl, size=(200, 40), label='发送')
        # 把两个按钮放到可伸缩的网格布局
        fgz2.Add(reset_btn, 1, wx.TOP | wx.LEFT)
        fgz2.Add(send_conn_btn, 1, wx.TOP | wx.RIGHT)
        # 将可伸缩的网格布局添加到box中
        box.Add(fgz2, 1, wx.ALIGN_CENTRE)
        #将盒子放到面板当中
        pl.SetSizer(box)
        '''---------------------------------------以上代码都是界面的绘制代码---------------------------------------------------'''
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_btn)
        #实例属性的设置
        self.client_name=client_name
        self.isConnected=False#存储客户端连接服务器的状态，默认为False，没有连接
        self.client_socket=None#设置客户端的socket对象为空
        #给发送按钮绑定一个事件
        self.Bind(wx.EVT_BUTTON, self.send_to_server, send_conn_btn)
        # 给断开按钮绑定一个事件
        self.Bind(wx.EVT_BUTTON, self.dis_conn_server, dis_conn_btn)
        # 给重置按钮绑定一个事件
        self.Bind(wx.EVT_BUTTON, self.reset, reset_btn)
    def reset(self,event):
        self.chat_text.Clear()#文本框中的内容就没有了

    def dis_conn_server(self,event):
        #发送断开的信息
        self.client_socket.send('Y_disconnect_SJ'.encode('utf-8'))
        #改变连接状态
        self.isConnected=False
    def send_to_server(self,event):
        #判断连接状态
        if self.isConnected:
            #从可写文本框中获取
            input_data= self.chat_text.GetValue()
            if input_data!='':
                 #向服务器发送数据
                self.client_socket.send(input_data.encode('utf-8'))
                #发完数据，清空文本框
                self.chat_text.SetValue('')

    def connect_to_server(self,event):
        print(f'客户端{self.client_name}连接服务器成功')
        #如果客户端没有连接服务器，则开始连接
        if not self.isConnected:
            #TCP编程的步骤
            server_host_port=('127.0.0.1',8888)
            #开始创建socket对象
            self.client_socket=socket(AF_INET,SOCK_STREAM)
            #发送连接请求
            self.client_socket.connect(server_host_port)
            #只要连接成功，必须发送一条数据
            self.client_socket.send(self.client_name.encode('utf-8'))
            #启动一个线程，客户端的线程与服务器的会话线程进行会话
            client_thread=threading.Thread(target=self.recv_data)
            #设置成守护线程，窗体关掉，子线程也结束
            client_thread.daemon=True
            #修改一下连接状态
            self.isConnected=True
            #启动线程
            client_thread.start()
    def recv_data(self):
        #如果是连接状态
        while self.isConnected:
            #接收来自服务器的数据
            data=self.client_socket.recv(1024).decode('utf-8')
            #显示到只读文本框中
            self.show_text.AppendText('-'*40+'\n'+data+'\n')

if __name__ == '__main__':
    #初始化APP（）
    app=wx.App()
    name=input('请输入客户端名称：')
    #创建自己的客户端界面对象
    client=YsjClient(name)
    client.Show()
    #循环刷新显示
    app.MainLoop()