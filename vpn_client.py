import socket
from cryptography.fernet import Fernet

# Get inputs from user
server_ip = input("Enter VPN server IP: ")
key = input("Enter encryption key: ")
message = input("Enter message to send: ")

# Setup encryption
fernet = Fernet(key)
encrypted_message = fernet.encrypt(message.encode())

# Send encrypted message
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((server_ip, 9999))
    client_socket.sendall(encrypted_message)
    print("✅ Message sent securely!")
