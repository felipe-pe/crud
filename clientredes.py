import socket
import sys

SERVER_PORT = 5432
MAX_LINE = 256

def main(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((host, SERVER_PORT))
    except Exception as e:
        print(f"Error connecting to server: {e}")
        sys.exit(1)
    
    print("Connected to server. Type your messages:")
    while True:
        msg = input()
        if not msg:
            break
        s.sendall(msg.encode('utf-8'))
    
    s.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <host>")
        sys.exit(1)
    
    main(sys.argv[1])
