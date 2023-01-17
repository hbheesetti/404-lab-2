import socket

BYTES_TO_READ = 4096

def get(host, port):
    request_data = b"GET / HTTP/1.1\nHOST:" + host.encode("utf-8")+ b"\n\n" # forming the request
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initialize the socket
    s.connect((host, port)) # connect to the right server and port in the server
    s.send(request_data) # send an request to the server
    s.shutdown(socket.SHUT_WR) # server stops listning 
    print("waiting for response")
    chunk = s.recv(BYTES_TO_READ) # accept a response from the server
    result = b'' + chunk

    while(len(chunk) > 0): # keep reading until we stop reciving the results from server
        chunk = s.recv(BYTES_TO_READ)
        result += chunk
    s.close() 

    return result


print(get("localhost", 80))