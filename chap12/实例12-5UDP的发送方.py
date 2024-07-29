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
from socket import socket,AF_INET,SOCK_DGRAM
#AF_INET表示internet通信
#SOCK_DGRAM（dgram）表示UDP连接
#（1）创建socket对象
send_socket=socket(AF_INET,SOCK_DGRAM)
#(2)准备发送数据
send_date=input('请输入要发送的数据:')
#(3)指定接收方的ip地址和端口
ip_port=('127.0.0.1',8888)
#发送数据
send_socket.sendto(send_date.encode('utf-8'),ip_port)
#接收来自接收方的回复数据，和接收方的地址
receive_data,addr=send_socket.recvfrom(1024)
print('接收到的来自接收方的数据为：',receive_data.decode('utf-8'))
print('接收方的地址为：',addr)
#(5)关闭socket对象
send_socket.close()