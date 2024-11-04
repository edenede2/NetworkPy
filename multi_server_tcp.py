import select
import socket


MAX_MSG_SIZE = 1024
IP = "0.0.0.0"
PORT = 5555

def print_client_sockets(open_client_sockets):
    print("Open client sockets:")
    for client_socket in open_client_sockets:
        print("\t", client_socket.getpeername())

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()

    print("Server is up and running")

    open_client_sockets = []
    messages_to_send = []

    while True:
        ready_to_read, ready_to_write, _ = select.select([server_socket] + open_client_sockets, open_client_sockets, [])

        for current_socket in ready_to_read:
            if current_socket is server_socket:
                client_socket, client_address = server_socket.accept()
                open_client_sockets.append(client_socket)
                print(f"Accepted connection from {client_address}")
            else:
                try:
                    data = current_socket.recv(MAX_MSG_SIZE).decode()
                except ConnectionResetError:
                    print(f"Connection with {current_socket} closed")
                    open_client_sockets.remove(current_socket)
                    current_socket.close()
                    print_client_sockets(open_client_sockets)
                    continue
                if data != "EXIT":
                    print(f"Received: {data} from {current_socket.getpeername()}")
                    
                    messages_to_send.append((current_socket, data))
                else:
                    print(f"Connection with {current_socket} closed")
                    current_socket.send("Bye".encode())
                    open_client_sockets.remove(current_socket)
                    current_socket.close()
                    print_client_sockets(open_client_sockets)
            
        for message in messages_to_send:
            client_socket, data = message
            if client_socket in ready_to_write:
                client_socket.send(data.encode())
                print(f"Sent: {data} to {client_socket.getpeername()}")
                messages_to_send.remove(message)
    


if __name__ == "__main__":
    main()
