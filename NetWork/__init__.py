"""
Core Python
"""
from socket import *
from time import ctime

HOST = ''  # 对bind()方法的标识, 表示可以使用任何可用的地址
PORT = 22222  # 随机
BUFSIZ = 2048  # 缓冲区大小, 单位是字节
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)  # 参数是在连接被转接或拒绝前, 传入连接请求的最大数

while 1:
    print('waiting for connecting....')
    tcpClisock, addr = tcpSerSock.accept()  # 客户端连接出现
    print('...connected from:', addr)

    while 1:
        data = tcpClisock.recv(BUFSIZ)
        if not data:  # 消息为空则意味着客户端退出
            break
        tcpClisock.send(
            bytes(ctime(), 'utf-8'), bytes(data, 'utf-8'))  # 加入时间戳
    tcpClisock.close()
tcpSerSock.close()



