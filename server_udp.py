import socket



IP = "0.0.0.0"
PORT = 8821
MAX_MSG_SIZE = 1024

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.bind((IP, PORT))

print("Server is up and running")

client_msg, client_address = my_socket.recvfrom(MAX_MSG_SIZE)
data = client_msg.decode()

print(f"Received: {data}")

response = "Super " + data

my_socket.sendto(response.encode(), client_address)

print(f"Sent: {response}")

my_socket.close()
