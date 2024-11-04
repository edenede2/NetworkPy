import socket

IP = "127.0.0.1"
PORT = 5555

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


my_socket.connect((IP, PORT))

data = ''

while data != 'Bye':
    data = input("Enter a message: ")

    my_socket.send(data.encode())

    data = my_socket.recv(1024).decode()

    print("The server sent: ", data)

print("Closing connection")
my_socket.close()

