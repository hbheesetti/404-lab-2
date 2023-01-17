import socket

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ) # recv info
            if not data:
                break
            print(data)
            conn.sendall(data) # send the data back

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # initializing it with a "with" block auto closes the socket after the use
        s.bind((HOST,PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # SO_REUSEADDR reuses the same address after a restart
        s.listen() #  in a state so can actively recieve requests 

        conn, addr = s.accept() # accept any incoming request
        handle_connection(conn, addr)

start_server()