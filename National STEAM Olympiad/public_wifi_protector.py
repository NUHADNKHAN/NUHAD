#The code is written by NUHAD N KhanN With his team members
import socket
import select

# Server configuration
SERVER_HOST = '127.0.0.1'  # Change this to your server's IP address
SERVER_PORT = 12345  # Change this to your desired port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to a specific address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"Listening on {SERVER_HOST}:{SERVER_PORT}...")

# List of sockets for select.select()
sockets_list = [server_socket]

# List of connected clients
clients = {}



def handle_client(client_socket):
    """Handles a single client connection"""
    try:
        # Receive data from the client
        data = client_socket.recv(4096)
        if data:
            # Send the received data to other connected clients
            for socket in clients:
                if socket != client_socket:
                    socket.send(data)
        else:
            # Remove the client socket from the list of sockets
            if client_socket in sockets_list:
                sockets_list.remove(client_socket)

            # Remove the client from the list of connected clients
            if client_socket in clients:
                del clients[client_socket]

            # Close the client socket
            client_socket.close()
    except Exception as e:
        print(f"Error handling client: {e}")


while True:
    # Get the list of sockets ready for reading
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()

            # Add the new client socket to the list of sockets
            sockets_list.append(client_socket)

            # Add the new client socket to the list of connected clients
            clients[client_socket] = client_address

            print(f"New connection from {client_address[0]}:{client_address[1]}")
        else:
            # Handle a client socket
            handle_client(notified_socket)
