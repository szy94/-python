import socket
#(1)创建socket对象
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#（2）使用bind绑定端口和ip
ip='127.0.0.1'
port=6666
server_socket.bind((ip,port))
#(3)listen
server_socket.listen(5)
print('服务器已启动')
#(4)accept
client_socket,client_ip=server_socket.accept()
#（5）rece（）send（）
receive_data=client_socket.recv(1024).decode('utf-8')#接收数据时应该从client_socket这个端口号中去接收
while receive_data!='bye':
    if receive_data!='':
        print('接受到的数据是：',receive_data)
    send_data=input('请输入要发送的数据：')
    client_socket.send(send_data.encode('utf-8'))#发送到client——socket对应的用户中，而不是server——socket.send
    if receive_data=='bye':
        break
    receive_data = client_socket.recv(1024).decode('utf-8')

#(6)close()
client_socket.close()
server_socket.close()
'''

'''