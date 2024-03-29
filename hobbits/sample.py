''' Demo code to interact with hobbits python package'''
import socket
from serializer import parse, marshall

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(('127.0.0.1', 9000))
SERVER.listen(5)


while True:
    CONN, ADDR = SERVER.accept()
    print("Received client's request")
    MSG = ''
    while True:
        DATA = CONN.recv(4096)
        print(DATA)
        if not DATA:
            break
        MSG += DATA.decode('utf-8')
    print(MSG)
    LEN_DATA = len(MSG)
    if LEN_DATA != 0:
        DECODED_MSG = parse(MSG)
        print(DECODED_MSG)
        ENCODED_MSG = marshall(DECODED_MSG)
        NEW_MSG = bytes(ENCODED_MSG, 'utf-8')
        print("Sending reponse back after parsing and marshalling")
        CONN.send(NEW_MSG)
