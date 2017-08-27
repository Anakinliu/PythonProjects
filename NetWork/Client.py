from socket import *

HOST = 'localhost'
PORT = 22222
BUFSIZ = 2048
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 分配TCP客户端套接字, 接着主动调用并连接到服务器
tcpCliSock.connect(ADDR)

while 1:
    data = input('> ')
    if not data:
        break  # 没有输入时退出
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break  # 服务器终止或者对recv()的调用失败
    print(data.decode('utf-8'))
tcpCliSock.close()
