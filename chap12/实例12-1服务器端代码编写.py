'''
socket对象的常用方法
方法名称                   功能描述
bind((ip, port))          绑定IP地址和端口
listen(N)              开始TCP监听，N表示操作系统挂起的最大连接数量，取值范围1-5之间，一般设置为5
accept（）              被动的接收TCP客户端的连接，阻塞式
connect((ip, port))      主动初始化TCP服务器连接
recv(size)                接收TCP数据，返回值为字符串类型，size表示要接收的最大数据量
recvfrom（）                  接收UDP数据，返回值为一个元组(data, address),data表示接收的数据，address表示发送数据的套接字地址
send(str)               发送TCP数据，返回值是要发送的字节数量
sendall(str)            完整发送TCP数据，将str中的数据发送到连接的套接字，返回之前尝试发送所有数据，如果成功为None，失败抛出异常
sendto(data, (ip, port))     发送UDP数据，返回值是发送的字节数
close()       关闭套接字
'''
'''
TCP服务器端流程如下：
1.使用socket类创建一个套接字对象
2.使用bind((ip, port))方法绑定IP地址和端口号
3.使用listen()方法开始TCP监听
4.使用accept()方法等待客户端的连接
5.使用recv()/send()方法接收/发送数据
6.使用close()关闭套接字
'''
'''
TCP客户端的流程如下：
1.使用socket类创建一个套接字对象
2.使用connect((host, port)设置连接的主机IP和主机设置的端口号
3.使用recv)/send)方法接收/发送数据
4.使用close()关闭套接字

'''
from socket import socket,AF_INET,SOCK_STREAM
#AF_INET用于internet之间的进程通信
#SOCK_STREAM（stream）表示用的TCP协议

#（1）使用socket类创建一个套接字对象
server_socket=socket(AF_INET,SOCK_STREAM)#表示用于internet之间的进程通信，用的TCP协议
#（2）使用bind((ip, port))方法绑定IP地址和端口号
ip='127.0.0.1'
port=8888
server_socket.bind((ip,port))
#(3)使用listen()方法开始TCP监听（服务器端进行监听）
server_socket.listen(5)
print('服务器已启动')
#(4)使用accept()方法等待客户端的连接
client_socket,client_ip=server_socket.accept()#系列解包赋值
#（5）使用recv()方法接收来自客户端的数据
data=client_socket.recv(1024)# 接收TCP数据，返回值为字符串类型，size表示要接收的最大数据量
print('客户端发送过来的数据为：',data.decode('utf-8'))#解码。要求用户客户端发送过来的数据是使用utf-8进行编码的

#（6）使用close()关闭套接字
server_socket.close()
client_socket.close()