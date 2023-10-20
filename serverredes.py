import socket

SERVER_PORT = 5432
MAX_PENDING = 5
MAX_LINE = 256

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', SERVER_PORT))
    s.listen(MAX_PENDING)
    
    print(f"Server listening on port {SERVER_PORT}...")
    while True:
        client, address = s.accept()
        print(f"Accepted connection from {address}")
        
        data = client.recv(MAX_LINE)
        while data:
            print(data.decode('utf-8'))
            data = client.recv(MAX_LINE)
        
        client.close()

if __name__ == "__main__":
    main()
