import socket
import time as ti
import random as ra

NAME = 'SuperServer'






server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up and running")

client_socket, client_address = server_socket.accept()
print("Client connected")


data = ''
back_data = ''
while True:

    data = client_socket.recv(1024).decode()
    commends_dict = {
        'exit': 'exit the server',
        'NAME': f'The server name is {NAME}',
        'TIME': f'The current time is {ti.ctime()}',
        'RAND': 'A random number between 1 and 100 is ' + str(ra.randint(1, 100))
    }
    print(f"Received: {data}")
    if data in commends_dict.keys():
        back_data = commends_dict[data]
    else:
        back_data = 'Invalid command'

    if data == 'Bye':
        back_data = ' '
    
    if data == 'exit':
        print("Client disconnected")
        client_socket.send("Bye".encode())
        break

    client_socket.send(back_data.encode())
    print(f"Sent: {back_data}")

client_socket.close()
server_socket.close()