import socket

TCP_IP = '192.xxx.xxx.xxx'           #enter your device IP
TCP_PORT = 5005

BUFFER_SIZE = 20                       # Normally 1024, but we want fast response
while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #creating socket object with IPv4 packet
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)                                               #listen to connection from 1 client
    conn, addr = s.accept()
    print("Connection address:", addr)

    data = conn.recv(BUFFER_SIZE)
    if data:
       print ("received data:", data)
       conn.shutdown(socket.SHUT_WR)
       conn.close()
