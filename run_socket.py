import socket

# Define server address and port
server_address = ('localhost', 12345)  # Change the address and port as needed

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")

# Accept incoming connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

try:
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        
        # Process received data (implement your logic here)
        print("Received:", data.decode())
        
        # Send a response back to the client
        response = "Server received your message"
        client_socket.sendall(response.encode())
finally:
    # Clean up the connection
    client_socket.close()
    server_socket.close()