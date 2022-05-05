
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created Successfully....")

server.bind(('localhost', 9999))

server.listen(10)
print("Server Waiting for connection..")

while True:
    c, addr = server.accept()
    print("Connected with", addr)
    c.send('Thank you for connecting'.encode())
    c.close()
