import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('localhost',12345))

server_socket.listen()

print('Sever is listening...')

client_socket,address = server_socket.accept()
print(f"Connection from {address} has established")

data = client_socket.recv(1024).decode()
print('Recieved from Client',data)

client_socket.send("Hello from server".encode())

client_socket.close()
server_socket.close()