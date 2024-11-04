import socket

IP = "127.0.0.1"
PORT = 8821

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.sendto("Hello".encode(), (IP, PORT))

response, address = my_socket.recvfrom(1024)
data = response.decode()
print("The server sent: ", data)

print("Closing connection")
my_socket.close()