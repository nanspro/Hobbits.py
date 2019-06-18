''' Hobbits unit tests '''
from __future__ import print_function
import queue
from hobbits.serializer import parse, marshall
from hobbits.server import start_server, start_client


def test_parsing():
    ''' Test for decoding a client request message '''

    msg = 'EWP 0.2 RPC 0 25\n{"id":1,"method_id":0x00}'
    msg2 = 'EWP 0.2 RPC 0 27\n<27 bytes binary body data>'
    msg3 = 'EWP 0.2 GOSSIP 25 16\n25 bytes of binary header\n16 bytes of body'

    if parse(msg) != {'protocol': 'EWP',
                      'call': 'RPC', 'version': '0.2',
                      'headers': '', 'body': '{"id":1,"method_id":0x00}'}:
        raise AssertionError()
    if parse(msg2) != {'protocol': 'EWP', 'call': 'RPC',
                       'version': '0.2', 'headers': '',
                       'body': '<27 bytes binary body data>'}:
        raise AssertionError()
    if parse(msg3) != {'protocol': 'EWP', 'call': 'GOSSIP',
                       'version': '0.2',
                       'headers': '25 bytes of binary header',
                       'body': '16 bytes of body'}:
        raise AssertionError()


def test_marshall():
    ''' Test for encoding a message to send to any node '''

    msg = {'protocol': 'EWP', 'call': 'RPC',
           'version': '0.2', 'headers': '',
           'body': '{"id":1,"method_id":0x00}'}
    msg2 = {'protocol': 'EWP', 'call': 'RPC',
            'version': '0.2', 'headers': '',
            'body': '<27 bytes binary body data>'}
    msg3 = {'protocol': 'EWP', 'call': 'GOSSIP',
            'version': '0.2', 'headers': '25 bytes of binary header',
            'body': '14 bytes of bo'}

    if marshall(msg) != \
            'EWP 0.2 RPC 0 25\n{"id":1,"method_id":0x00}':
        raise AssertionError()
    if marshall(msg2) != \
            'EWP 0.2 RPC 0 27\n<27 bytes binary body data>':
        raise AssertionError()
    if marshall(msg3) != \
            'EWP 0.2 GOSSIP 25 14\n25 bytes of binary header\n14 bytes of bo':
        raise AssertionError()


def test_tcp():
    ''' Testing tcp transport between a client and a server '''
    que = queue.Queue()
    t_1 = start_server(que, '127.0.0.1', 65410, 10)
    t_1.start()

    msg = b'EWP 0.2 RPC 0 25\n{"id":1,"method_id":0x00}'
    t_2 = start_client('127.0.0.1', 65410, msg)
    t_2.start()
    t_2.join()
    t_1.join()
    result = que.get()
    if result != msg:
        raise AssertionError()
