''' TCP client server methods'''
import socket
import threading
from hobbits.serializer import parse, marshall


def create():
    ''' Create a socket for TCP transport'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return server


def start_server(que, host, port, queue_size):
    ''' Create a thread for server by providing a queue and callback'''
    t_1 = threading.Thread(
        target=lambda q, arg1, arg2, arg3: q.put(handle_server(arg1,
                                                               arg2, arg3)),
        args=(que, host, port, queue_size))
    return t_1


def start_client(host, port, msg):
    ''' Create a thread for client by providing callback'''
    t_1 = threading.Thread(target=handle_client, args=(host, port, msg))
    return t_1


def handle_server(host, port, queue_size):
    ''' Server socket listens for connections and then first
    decode the message and then encode it again to
    send to client '''
    server = create()
    server.bind((host, port))
    server.listen(queue_size)

    conn, _addr = server.accept()
    print("Received client's request")
    msg = ''
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode('utf-8')
    print(msg)
    decoded_msg = parse(msg)
    print(decoded_msg)
    encoded_msg = marshall(decoded_msg)
    print(encoded_msg)
    new_msg = bytes(encoded_msg, 'utf-8')
    print(new_msg)
    return new_msg
    # conn.sendall(new_msg)


def handle_client(host, port, msg):
    ''' Client socket connects to host and port
    and sends an message '''
    client = create()
    client.connect((host, port))
    client.sendall(msg)
    print("client sent message")
    # tmp = client.recv(1024)
    # print("received message from server")
    # _data = tmp.decode('utf-8')
    # assert _data == msg
