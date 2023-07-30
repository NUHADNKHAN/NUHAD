import socket
import threading

class Firewall:
    def __init__(self):
        self.allowed_ports = [80, 443]  # Ports to be allowed

    def is_allowed(self, port):
        return port in self.allowed_ports

    def start_firewall(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 8080))
        server_socket.listen(5)

        print("Firewall started. Listening on port 8080...")

        while True:
            client_socket, client_address = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024)
        port = self.get_port_from_request(request_data)
        
        if self.is_allowed(port):
            print(f"Allowing connection to port {port}")
            client_socket.send(b"HTTP/1.1 200 OK\r\n\r\n")
        else:
            print(f"Blocking connection to port {port}")
            client_socket.send(b"HTTP/1.1 403 Forbidden\r\n\r\n")

        client_socket.close()

    def get_port_from_request(self, request_data):
        try:
            # Parse the request to find the port number (assuming simple HTTP request)
            request_str = request_data.decode("utf-8")
            port_start = request_str.find(":")

            if port_start != -1:
                port_end = request_str.find(" ", port_start)
                port_str = request_str[port_start + 1:port_end]
                port = int(port_str)
                return port
            else:
                return None

        except Exception as e:
            print("Error parsing request:", e)
            return None


if __name__ == "__main__":
    firewall = Firewall()
    firewall.start_firewall() 
