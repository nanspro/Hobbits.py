import socket, threading
from Serializer import parse, marshall

def create():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return server

def start_server(host, port, queue_size):
    t1 = threading.Thread(target=handle_server, args=(host, port, queue_size))
    return t1

def start_client(host, port, msg):
    t1 = threading.Thread(target=handle_client, args=(host, port, msg))
    return t1

def handle_server(host, port, queue_size):
    server = create()
    server.bind((host, port))    
    server.listen(queue_size)

    conn, addr = server.accept()
    print("Received client's request")
    msg = ''
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode('utf-8')
    # print(msg)
    decoded_msg = parse(msg)
    # print(decoded_msg)
    encoded_msg = marshall(decoded_msg)
    # print(encoded_msg)
    new_msg = bytes(encoded_msg, 'utf-8')
    # print(new_msg)
    conn.sendall(new_msg)

def handle_client(host, port, msg):
    client = create()
    client.connect((host, port))
    client.sendall(msg)
    print("client is sending message")
    tmp = client.recv(1024)
    print("received message from server")
    data = tmp.decode('utf-8')
    # assert data == msg