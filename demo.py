import socket
from serializer import parse, marshall

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9000))    
server.listen(5)


while True:
    conn, ADDR = server.accept()
    print("Received client's request")
    MSG = ''
    DATA = conn.recv(4096)
    MSG += DATA.decode('utf-8')
    DECODED_MSG = parse(MSG)
    ENCODED_MSG = marshall(DECODED_MSG)
    NEW_MSG = bytes(ENCODED_MSG, 'utf-8')
    print("Sending reponse back after parsing and marshalling")
    conn.sendall(NEW_MSG)
    conn.close()
