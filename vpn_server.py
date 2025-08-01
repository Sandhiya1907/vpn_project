import socket
from cryptography.fernet import Fernet

print("✅ Server script started")

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

print("🔐 Share this key with the client:", key.decode())

# Setup server socket
server = socket.socket()
server.bind(("0.0.0.0", 9999))
server.listen(1)

print("📡 Listening on port 9999...")

# Accept a connection
conn, addr = server.accept()
print("✅ Client connected from:", addr)

# Send key to client (optional)
# conn.send(key)  # you may skip this if key is shared manually

# Receive and decrypt messages
while True:
    encrypted = conn.recv(4096)
    if not encrypted:
        break
    decrypted = cipher.decrypt(encrypted)
    print("📥 Received:", decrypted.decode())
